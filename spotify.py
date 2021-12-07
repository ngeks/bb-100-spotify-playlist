import requests

BASE_URL = "https://api.spotify.com"
BROWSER_PATH = "YOUR_BROWSER_PATH_HERE %s"


class Spotify:
    def __init__(self):
        self.response_type = "token"
        self.redirect_uri = "http://example.com"
        self.show_dialog = True
        self.scope = "user-read-private playlist-modify-private"
        self.bearer_token = None
        self.uid = None

    def authorize(self, client_id):
        """Authorize program to access your Spotify account."""
        url = "https://accounts.spotify.com/authorize?"
        url += f"client_id={client_id}"
        url += f"&response_type={self.response_type}"
        url += f"&redirect_uri={self.redirect_uri}"
        url += f"&show_dialog={self.show_dialog}"
        url += f"&scope={self.scope}"

        import webbrowser as wb
        wb.get(BROWSER_PATH).open(url)

    def set_uid(self):
        """Get current user id."""
        url = BASE_URL + "/v1/me"
        headers = {'Authorization': f"Bearer {self.bearer_token}"}

        resp = requests.get(
            url,
            headers=headers
        )
        self.uid = resp.json()['id']

    def authenticate(self, token):
        """Set access token and user id."""
        self.bearer_token = token
        self.set_uid()

    def create_playlist(self, date):
        """Create spotify playlist."""
        url = BASE_URL + f"/v1/users/{self.uid}/playlists"
        headers = {'Authorization': f"Bearer {self.bearer_token}", 'Content-Type': "application/json"}
        data = {
            'name': f"Billboard Top 100 ({date})",
            'description': f"A playlist of billboard top 100 songs as of {date}.",
            'public': False
        }

        resp = requests.post(
            url,
            headers=headers,
            json=data
        )
        return resp.json()['id']

    def search_track_id(self, track, year):
        """Search for track. If found, get track id."""
        url = BASE_URL + "/v1/search"
        headers = {'Authorization': f"Bearer {self.bearer_token}"}
        params = {'q': f"track:{track} year:{year}", 'type': "track"}

        resp = requests.get(
            url,
            headers=headers,
            params=params
        )
        return f"spotify:track:{resp.json()['tracks']['items'][0]['id']}"

    def add_track_to_playlist(self, playlist_id, track):
        """Add track to playlist."""
        url = BASE_URL + f"/v1/playlists/{playlist_id}/tracks"
        headers = {'Authorization': f"Bearer {self.bearer_token}"}
        params = {'uris': track}

        resp = requests.post(
            url,
            headers=headers,
            params=params
        )
        return resp.json()['snapshot_id']
    