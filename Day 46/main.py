from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/india-songs-hotw/{date}/")
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name='h3', id='title-of-a-story', class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify Authentication
SPOTIPY_CLIENT_ID = 'id'
SPOTIPY_CLIENT_SECRET = 'secret'
SPOTIPY_REDIRECT_URI = 'http://example.com'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Get current user ID
user_id = sp.current_user()["id"]
print(f"User ID: {user_id}")

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist created: {playlist['name']}")

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Songs have been added to the playlist.")
