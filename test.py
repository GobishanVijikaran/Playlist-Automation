import requests
import json
from secrets import spotify_token, spotify_user_id

query = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
request_body = json.dumps({
    "name": "Test Playlist",
    "description": "Creating a test playlist with Spotify api",
    "public": False
    })

header = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    "Authorization":"Bearer {}".format(spotify_token)
}

response = requests.post(
    url=query,
    data=request_body,
    headers=header)
print(response)
response_mod = response.json()
print(response_mod)
playlist_id = response_mod["id"]

# Search for songs
song_name = "say my name"
song_type = "track"
song_market = "US"
sng_id = 'id'
get_song_query = f"https://api.spotify.com/v1/search?q={song_name}&type={song_type}&market={song_market}&limit=1"
get_song = requests.get(url=get_song_query, headers=header)
get_song_mod = get_song.json()
song_id = get_song_mod["tracks"]["items"][0]["uri"]
print(song_id)


# Adding to Playlist
track_query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={song_id.replace(':', '%3A')}"
add_tracks = requests.post(url=track_query, headers=header)
print(add_tracks)