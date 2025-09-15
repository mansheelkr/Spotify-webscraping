import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from pprint import pprint

# STEP 1: SCRAPING THE BILLBOARD HOT 100
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
URL = f"https://www.billboard.com/charts/hot-100/{user_date}/"
response = requests.get(url=URL, headers=header)
songs_webpage = response.text

soup = BeautifulSoup(songs_webpage, "html.parser")

all_songs = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
#print(all_songs)

top_100_songs = []

for song in all_songs:
  song_title = song.getText()
  song_title = song_title.strip()
  top_100_songs.append(song_title)

print(top_100_songs)

# STEP 2: AUTHETICATION WITH SPOTIFY
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username="31nfhedamszpbzvjovzy7e25jx5q", 
    )
)

user_id = sp.current_user()["id"]
print(user_id)

# STEP 3: SEARCH SPOTIFY FOR THE SONGS FROM STEP 1
song_uris = []
year = user_date.split("-")[0]


for song in top_100_songs:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# STEP 4: CREATING AND ADDING TO SPOTIFY PLAYLIST
playlist = sp.user_playlist_create(user=user_id, name=f'{user_date} Billboard 100', public=False, collaborative=False, description='')

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)