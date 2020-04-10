# Add Docstring explaining the script
import os
import json
import requests
from secrets import spotify_token, spotify_user_id


class PlaylistAutomation:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.spotify_token = spotify_token
        pass

    def login_youtube(self):
        pass

    # https://developers.google.com/youtube/v3/docs/playlists
    def get_liked_videos(self):
        pass

    def yt_playlist(self):
        pass

    def get_song(self):

        song_name = "toosie slide"
        song_type = "track"
        song_market = "US"

        get_song_query = f"https://api.spotify.com/v1/search?q={song_name}&type={song_type}&market={song_market}&limit=1"
        get_song = requests.get(url=get_song_query, headers=http_header)
        get_song_mod = get_song.json()
        song_id = get_song_mod["tracks"]["items"][0]["uri"]

        # Adding to Playlist
        track_query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={song_id.replace(':', '%3A')}"
        add_tracks = requests.post(url=track_query, headers=http_header)
        print(add_tracks)

    def spotify_playlist(self):
        query = f"https://api.spotify.com/v1/users/{self.spotify_user_id}/playlists"

        request_body = json.dumps({
            "name": "YouTube Playlist",
            "description": "Songs from your Youtube playlist now on Spotify",
            "public": False
        })

        http_header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        }

        response = requests.post(url=query, data=request_body, headers=http_header)
        response_mod = response.json()
        playlist_id = response_mod["id"]

        # Adding to Playlist
        track_uri = "spotify:track:6rqhFgbbKwnb9MLmUQDhG6"
        track_query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={track_uri.replace(':', '%3A')}"
        add_tracks = requests.post(url=track_query, headers=http_header)
