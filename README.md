<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Billboard_Top_100_Spotify_Playlist_0"></a>Billboard Top 100 (Spotify Playlist)</h1>
<p class="has-line-data" data-line-start="1" data-line-end="3"><a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="made-with-python"></a> <a href="https://github.com/ngeks/bb-100-spotify-playlist/blob/main/LICENSE"><img src="https://badgen.net/github/license/Naereen/Strapdown.js" alt="GitHub license"></a> <a href="https://saythanks.io/to/ngeksdev"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks!"></a><br>
<a href="https://www.buymeacoffee.com/ngeks"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="&amp;quot;Buy Me A Coffee&amp;quot;"></a></p>
<p class="has-line-data" data-line-start="4" data-line-end="5">A python script that can easily generate a spotify playlist of billboard’s top 100 songs as of date given by user. Created with Python and BeautifulSoup4 module following object-oriented programming.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="How_to_run_the_script_6"></a>How to run the script?</h2>
<h3 class="code-line" data-line-start=7 data-line-end=8 ><a id="Requirements_7"></a>Requirements</h3>
<ul>
<li class="has-line-data" data-line-start="8" data-line-end="9">You must have <code>python</code> installed on your computer.</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">You must have <code>pip</code> installed on your computer.</li>
<li class="has-line-data" data-line-start="10" data-line-end="12">You must have a <a href="https://developer.spotify.com/">Spotify Developer</a> account.</li>
</ul>
<h3 class="code-line" data-line-start=12 data-line-end=13 ><a id="Instructions_12"></a>Instructions</h3>
<ol>
<li class="has-line-data" data-line-start="13" data-line-end="16">
<p class="has-line-data" data-line-start="13" data-line-end="15">First, clone the repository.<br>
<code>git clone https://github.com/ngeks/bb-100-spotify-playlist.git</code></p>
</li>
<li class="has-line-data" data-line-start="16" data-line-end="19">
<p class="has-line-data" data-line-start="16" data-line-end="18">Then, navigate inside the folder.<br>
<code>cd bb-100-spotify-playlist</code></p>
</li>
<li class="has-line-data" data-line-start="19" data-line-end="22">
<p class="has-line-data" data-line-start="19" data-line-end="21">Install required packages.<br>
<code>pip install -r requirements.txt</code></p>
</li>
<li class="has-line-data" data-line-start="22" data-line-end="26">
<p class="has-line-data" data-line-start="22" data-line-end="23">Create a new application in your <a href="https://developer.spotify.com/">Spotify Developer</a> dashboard.</p>
<p class="has-line-data" data-line-start="24" data-line-end="25"><img src="https://i.imgur.com/ykIQwT0.png" alt=""></p>
</li>
<li class="has-line-data" data-line-start="26" data-line-end="30">
<p class="has-line-data" data-line-start="26" data-line-end="27">Copy your <code>Client ID</code> and paste it inside <code>main.py</code> file.</p>
<p class="has-line-data" data-line-start="28" data-line-end="29"><img src="https://i.imgur.com/MScJCzZ.png" alt=""></p>
</li>
<li class="has-line-data" data-line-start="30" data-line-end="35">
<p class="has-line-data" data-line-start="30" data-line-end="32">Add redirect URI to application settings.<br>
<em>Use <code>http://example.com</code> if you do not have a Redirect URI.</em></p>
<p class="has-line-data" data-line-start="33" data-line-end="34"><img src="https://i.imgur.com/G3hW9mP.png" alt=""></p>
</li>
<li class="has-line-data" data-line-start="35" data-line-end="43">
<p class="has-line-data" data-line-start="35" data-line-end="36">Add your browser path in <code>python.py</code> file.</p>
<p class="has-line-data" data-line-start="37" data-line-end="42"><em>Example:</em><br>
<strong>Firefox (Windows 11)</strong><br>
<code>&quot;C:/Program Files/Firefox Developer Edition/firefox.exe&quot;</code><br>
<strong>Google Chrome (Windows 11)</strong><br>
<code>&quot;C:/Program Files/Google/Chrome/Application/chrome.exe&quot;</code></p>
</li>
<li class="has-line-data" data-line-start="43" data-line-end="55">
<p class="has-line-data" data-line-start="43" data-line-end="45">Run the script.<br>
<code>python main.py</code></p>
<p class="has-line-data" data-line-start="46" data-line-end="47"><img src="https://i.imgur.com/1fcV3E1.png" alt=""></p>
<p class="has-line-data" data-line-start="48" data-line-end="49"><em>After entering a date your browser will open the spotify authorization request page.</em></p>
<p class="has-line-data" data-line-start="50" data-line-end="51"><img src="https://i.imgur.com/XiyJW6N.png" alt=""></p>
<p class="has-line-data" data-line-start="52" data-line-end="54"><em>Click the agree button.</em><br>
<em>The page will then redirect you to your redirect URI.</em></p>
</li>
<li class="has-line-data" data-line-start="55" data-line-end="67">
<p class="has-line-data" data-line-start="55" data-line-end="56">Copy the access token from the page URL where you got redirected.</p>
<p class="has-line-data" data-line-start="57" data-line-end="58"><strong>URL</strong></p>
<pre><code class="has-line-data" data-line-start="59" data-line-end="61">http://example.com/#access_token=BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g&amp;token_type=Bearer&amp;expires_in=3600
</code></pre>
<p class="has-line-data" data-line-start="62" data-line-end="63"><strong>ACCESS TOKEN</strong></p>
<pre><code class="has-line-data" data-line-start="64" data-line-end="66">BQBKjzU45tSYvvIcrGDZPwpAofjaunbvXzAKMPBNvceW6pxFu0JN3NrFqrgxeab3jzNxJb6xbXLjI4FqfgDG2wEijb0ncmpuXG_-GREg_gY1fyMYf7q1ZaWYvNyh4X83DIMHe-nD-Cq8lz9Ep6us1hQhKXjZWO_x05Nru_4xZJESoNRvQNxjq4bazRONHZ_QhIeSsLDG6g
</code></pre>
</li>
<li class="has-line-data" data-line-start="67" data-line-end="71">
<p class="has-line-data" data-line-start="67" data-line-end="68">Paste your access token.</p>
<p class="has-line-data" data-line-start="69" data-line-end="70"><img src="https://i.imgur.com/cyKv34h.png" alt=""></p>
</li>
<li class="has-line-data" data-line-start="71" data-line-end="75">
<p class="has-line-data" data-line-start="71" data-line-end="72">Wait for the program to finish process.</p>
<p class="has-line-data" data-line-start="73" data-line-end="74"><img src="https://i.imgur.com/emNCpVv.gif" alt=""></p>
</li>
</ol>
<h2 class="code-line" data-line-start=75 data-line-end=76 ><a id="License_75"></a>License</h2>
<p class="has-line-data" data-line-start="76" data-line-end="77">Distributed under <a href="https://github.com/ngeks/bb-100-spotify-playlist/blob/main/LICENSE">MIT License</a>.</p>
<h2 class="code-line" data-line-start=78 data-line-end=79 ><a id="Links_78"></a>Links</h2>
<p class="has-line-data" data-line-start="79" data-line-end="82">Repository: <a href="https://github.com/ngeks/bb-100-spotify-playlist">https://github.com/ngeks/bb-100-spotify-playlist</a><br>
Twitter: <a href="https://twitter.com/ngeksdev">@ngeksdev</a><br>
Email: <a href="mailto:ngeksdev@gmail.com">ngeksdev@gmail.com</a></p>
