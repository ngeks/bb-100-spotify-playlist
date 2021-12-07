from datetime import datetime
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"


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

    # print(tracks_title)


if __name__ == '__main__':
    main()
