# Add Docstring explaining the script
import os
import urllib.request
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Create Class (always running?)
# Login to Youtube
# Liked Videos (songs)
# Create new playlist
# Search for song
# Create new playlist

class PlaylistAutomation:
    def __init__(self):
        pass
    def login_youtube(self):
        pass

    # https://developers.google.com/youtube/v3/docs/playlists
    def get_liked_videos(self):
        pass
    def yt_playlist(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        secrets_file = "secrets.json"


        pass
    def get_song(self):
        pass
    def spotify_playlist(self):
        pass
