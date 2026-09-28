import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

date = input("Which year do you want to be transported to? Type the date in this format(YYYY-MM-DD): ")
print(date)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}

response = requests.get("https://appbrewery.github.io/bakeboard-hot-100/" + date, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)
all_song_title_headings = soup.find_all("h3", class_="chart-entry__title")
hot_100_songs = [heading.text for heading in all_song_title_headings]
print(hot_100_songs)

yt_music = YTMusic("browser.json")
new_playlist_name = f"{date} Billboard 100"
playlist_id = ""

library_playlists = yt_music.get_library_playlists()
print(library_playlists)

for playlist in library_playlists:
    if playlist["title"] == new_playlist_name:
        playlist_id = playlist["playlistId"]
        break

if playlist_id == "":
    playlist_id = yt_music.create_playlist(new_playlist_name, f"Lists top 100 songs from {date}")
    print(f"Created {new_playlist_name} with {playlist_id}")

for song in hot_100_songs:
    try:
        search_results = yt_music.search(song, filter="songs", limit=1)
        yt_music.add_playlist_items(playlist_id, [search_results[0]['videoId']])
        print(f"Added {song} to {new_playlist_name}")
    except Exception as e:
        print(f"Skipped {song} | Reason: {e}")



