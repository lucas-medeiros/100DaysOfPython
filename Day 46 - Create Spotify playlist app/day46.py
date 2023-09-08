# @author   Lucas Cardoso de Medeiros
# @since    07/12/2022
# @version  1.0

# Create Spotify Playlist using the Musical Time Machine

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100"

SPOTIPY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIPY_SCOPE = "playlist-modify-private"


def get_date():
    return input("Which year do you want do travel to? Type the date in this format YYYY-MM-DD: ")


def get_songs(date):
    """Scraping Billboard 100"""
    url = f"{URL}/{date}/"
    print(url)
    response = requests.get(url)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    songs_spans = soup.find_all(name="h3", id="title-of-a-story", class_="a-truncate-ellipsis")
    return [title.getText().strip() for title in songs_spans]


def spotify_login():
    """Spotify Authentication"""
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=SPOTIPY_SCOPE,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path=".cache"
        )
    )


def get_songs_uris(songs, year, sp):
    """Searching Spotify for songs by title"""
    uris = []
    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return uris


def create_playlist(user, name, public):
    """Creating a new playlist in Spotify"""
    return sp.user_playlist_create(user=user, name=name, public=public)


def add_songs_to_playlist(sp, user, playlist_id, songs):
    """Adding songs found into the new playlist"""
    return sp.user_playlist_add_tracks(user=user, playlist_id=playlist_id, tracks=songs)


if __name__ == "__main__":
    date = get_date()
    songs = get_songs(date)

    sp = spotify_login()
    user_id = sp.current_user()["id"]
    songs_uris = get_songs_uris(songs, date.split("-")[0], sp)
    print(songs_uris)

    playlist_name = f"{date} Billboard 100"
    playlist = create_playlist(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
    add_playlist = add_songs_to_playlist(sp=sp, user=user_id, playlist_id=playlist["id"], songs=songs_uris)
    print(add_playlist)
