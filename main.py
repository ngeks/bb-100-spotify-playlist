from datetime import datetime
from bs4 import BeautifulSoup

from spotify import Spotify

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = "YOUR_CLIENT_ID_HERE"


def main():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            delta = datetime.strptime(date, "%Y-%m-%d")
            if delta > datetime.today():
                raise ValueError
        except ValueError:
            print("Invalid date. Try again.\n")
        else:
            break

    import requests
    html_doc = requests.get(BILLBOARD_URL + f"/{date}")

    bs1 = BeautifulSoup(html_doc.text, "html.parser")
    blocks = bs1.find_all("div", class_="o-chart-results-list-row-container")
    tracks_title = []

    for block in blocks:
        bs2 = BeautifulSoup(str(block), "html.parser")
        title = bs2.find("h3", class_="c-title").get_text().strip()
        tracks_title.append(title)

    sp = Spotify()
    sp.authorize(CLIENT_ID)

    token = input("Enter access token: ")

    try:
        sp.authenticate(token)
    except KeyError:
        print("Invalid access token.")
        return
    else:
        playlist_id = sp.create_playlist(date)

    year = date.split("-")[0]
    tracks = []

    print("\nSearching for tracks ids...")
    for track in tracks_title:
        try:
            tracks.append(sp.search_track_id(track, year))
        except IndexError:
            print(f"\"{track}\" not found. Skipped.")
            pass
        else:
            print(f"\"{track}\" added to queue.")

    print("\nInsert tracks to playlist...\n")
    for track in tracks:
        sp.add_track_to_playlist(playlist_id, track)
        print(f"{track} added to playlist: {playlist_id}")


if __name__ == '__main__':
    main()
