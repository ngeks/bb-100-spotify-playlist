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
