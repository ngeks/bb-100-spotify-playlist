<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Billboard_Top_100_Spotify_Playlist_0"></a>Billboard Top 100 (Spotify Playlist)</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2"><a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="made-with-python"></a> <a href="https://github.com/Naereen/StrapDown.js/blob/master/LICENSE"><img src="https://badgen.net/github/license/Naereen/Strapdown.js" alt="GitHub license"></a> <a href="https://saythanks.io/to/ngeksdev"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks!"></a></p>
<p class="has-line-data" data-line-start="3" data-line-end="4">A python script that can easily generate a spotify playlist of billboard’s top 100 songs as of date given by user. Created with Python and BeautifulSoup4 module following object-oriented programming.</p>
<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="How_to_run_the_script_5"></a>How to run the script?</h2>
<h3 class="code-line" data-line-start=6 data-line-end=7 ><a id="Requirements_6"></a>Requirements</h3>
<ul>
<li class="has-line-data" data-line-start="7" data-line-end="8">You must have <code>python</code> installed in your computer.</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">You must have <code>pip</code> installed in your computer.</li>
<li class="has-line-data" data-line-start="9" data-line-end="11">You must have a <a href="https://developer.spotify.com/">Spotify Developer</a> account.</li>
</ul>
<h3 class="code-line" data-line-start=11 data-line-end=12 ><a id="Instructions_11"></a>Instructions</h3>
<ol>
<li class="has-line-data" data-line-start="12" data-line-end="14">Clone repository.<br>
<code>git clone https://github.com/ngeks/bb-100-spotify-playlist.git</code></li>
<li class="has-line-data" data-line-start="14" data-line-end="16">Navigate inside repository folder.<br>
<code>cd bb-100-spotify-playlist</code></li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Go to to your <a href="https://developer.spotify.com/">Spotify Developer</a> dashboard.</li>
<li class="has-line-data" data-line-start="17" data-line-end="19">Create a new application.<br>
<img src="https://i.imgur.com/ykIQwT0.png" alt=""></li>
<li class="has-line-data" data-line-start="19" data-line-end="21">Copy your client id then paste it inside <code>main.py</code><br>
<img src="https://i.imgur.com/MScJCzZ.png" alt=""></li>
<li class="has-line-data" data-line-start="21" data-line-end="23">Add redirect URI to application settings. If you do not have your own callback URI use <code>http://example.com</code><br>
<img src="https://i.imgur.com/G3hW9mP.png" alt=""></li>
<li class="has-line-data" data-line-start="23" data-line-end="28">Add your browser path in <code>python.py</code>. See example below.<br>
<strong>Firefox</strong><br>
<strong>Windows 11</strong>: <code>&quot;C:/Program Files/Firefox Developer Edition/firefox.exe&quot;</code><br>
<strong>Google Chrome</strong><br>
<strong>Windows 11</strong>: <code>&quot;C:/Program Files/Google/Chrome/Application/chrome.exe&quot;</code></li>
<li class="has-line-data" data-line-start="28" data-line-end="35">Run the script and enter desired date.<br>
<code>python main.py</code><br>
<img src="https://i.imgur.com/1fcV3E1.png" alt=""><br>
<em>After entering a date your browser will open the spotify authorization request page.</em><br>
<img src="https://i.imgur.com/XiyJW6N.png" alt=""><br>
<em>Click the agree button.</em><br>
<em>The page will then redirect you to your redirect URI.</em></li>
<li class="has-line-data" data-line-start="35" data-line-end="38">Copy the access token from the page URL where you got redirected.<br>
<strong>URL</strong>: <code>http://example.com/#access_token=BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g&amp;token_type=Bearer&amp;expires_in=3600</code><br>
<strong>Access Token</strong>: <code>BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g</code></li>
<li class="has-line-data" data-line-start="38" data-line-end="40">Paste your access token.<br>
<img src="https://i.imgur.com/cyKv34h.png" alt=""></li>
<li class="has-line-data" data-line-start="40" data-line-end="43">Wait for the program to finish process.<br>
<img src="https://i.imgur.com/emNCpVv.gif" alt=""></li>
</ol>
<h2 class="code-line" data-line-start=43 data-line-end=44 ><a id="License_43"></a>License</h2>
<p class="has-line-data" data-line-start="44" data-line-end="45">Distributed under <a href="https://github.com/ngeks/bb-100-spotify-playlist/blob/main/LICENSE">MIT License</a>.</p>
<h2 class="code-line" data-line-start=46 data-line-end=47 ><a id="Contacts_46"></a>Contacts</h2>
<p class="has-line-data" data-line-start="47" data-line-end="51"><a href="https://ko-fi.com/V7V57APFI"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi"></a><br>
Repository Link: <a href="https://github.com/ngeks/bb-100-spotify-playlist">https://github.com/ngeks/bb-100-spotify-playlist</a><br>
Twitter: <a href="https://twitter.com/ngeksdev">@ngeksdev</a><br>
Email: <a href="mailto:ngeksdev@gmail.com">ngeksdev@gmail.com</a></p>