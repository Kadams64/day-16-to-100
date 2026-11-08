import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

BAKEBOARD_BASE_URL = "https://appbrewery.github.io/bakeboard-hot-100"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
}

# Optional Troubleshooting Step - Check for browser.json before doing anything else
if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()
'''from project directory:
pbpaste | /Users/kelly/PycharmProjects/day-16-to-100/.venv/bin/ytmusicapi browser'''

date_string = input("Date to travel to (YYYY-MM-DD): ")

response = requests.get(f"{BAKEBOARD_BASE_URL}/{date_string}", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# single entry looks like this
"""<h3 class="chart-entry__title">Choosin' Texas</h3>"""

songs = soup.select(".chart-entry__title")

# for song in songs:
#     print(song.text)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()

playlist_name = f"{date_string} Billboard top 100"

playlist_exists = False
playlist_id = None
for playlist in playlists:
    if playlist_name == playlist["title"]:
        playlist_exists = True
        playlist_id = playlist["playlistId"]
        print(playlist_id)

if not playlist_exists:
    playlist_id = yt.create_playlist(
        title=playlist_name, description="Top 100 list for noted date"
    )
    print(playlist_id)
else:
    print("Playlist already exists.")

matches = []
for song in songs:
    title = song.text
    try:
        matches = yt.search(query=title, filter="songs", limit=1)
        # print(matches)
        yt.add_playlist_items(playlistId=playlist_id, videoIds=[matches[0]["videoId"]])
        print(f"added: {title}")
    except Exception as e:
        print(e)