# Billboard Top 100 (Spotify Playlist)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/ngeksdev)

A python script that can easily generate a spotify playlist of billboard's top 100 songs as of date given by user. Created with Python and BeautifulSoup4 module following object-oriented programming.

## How to run the script?
### Requirements
- You must have `python` installed in your computer.
- You must have `pip` installed in your computer.
- You must have a [Spotify Developer](https://developer.spotify.com/) account.

### Instructions
1. Clone repository.
`git clone https://github.com/ngeks/bb-100-spotify-playlist.git`
2. Navigate inside repository folder.
`cd bb-100-spotify-playlist`
3. Go to to your [Spotify Developer](https://developer.spotify.com/) dashboard.
4. Create a new application.
   ![](https://i.imgur.com/ykIQwT0.png)
5. Copy your client id then paste it inside `main.py`
    ![](https://i.imgur.com/MScJCzZ.png)
6. Add redirect URI to application settings. If you do not have your own callback URI use `http://example.com`
    ![](https://i.imgur.com/G3hW9mP.png)
7. Add your browser path in `python.py`. See example below.
**Firefox**
**Windows 11**: `"C:/Program Files/Firefox Developer Edition/firefox.exe"`
**Google Chrome**
**Windows 11**: `"C:/Program Files/Google/Chrome/Application/chrome.exe"`
8. Run the script and enter desired date. 
`python main.py`
![](https://i.imgur.com/1fcV3E1.png)
*After entering a date your browser will open the spotify authorization request page.*
![](https://i.imgur.com/XiyJW6N.png)
*Click the agree button.*
*The page will then redirect you to your redirect URI.*
9. Copy the access token from the page URL where you got redirected.
**URL**: `http://example.com/#access_token=BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g&token_type=Bearer&expires_in=3600`
**Access Token**: `BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g`
10. Paste your access token.
![](https://i.imgur.com/cyKv34h.png)
11. Wait for the program to finish process.
![](https://i.imgur.com/emNCpVv.gif)

## License
Distributed under [MIT License](https://github.com/ngeks/bb-100-spotify-playlist/blob/main/LICENSE).

## Contacts
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/V7V57APFI)
Repository Link: https://github.com/ngeks/bb-100-spotify-playlist
Twitter: [@ngeksdev](https://twitter.com/ngeksdev)
Email: ngeksdev@gmail.com

