import json
import requests
from argparse import ArgumentParser
from secrets import spotify_token, spotify_user_id, yt_api_key


class PlaylistConverter:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.youtube_token = yt_api_key

    def setup_args(self):
        """
        Setup command line arguments
        :return argparse:
        """
        parser = ArgumentParser(
            usage="For more information on how to use this script, type in either '-h' or '--help'!")

        # Mandatory Argument
        parser.add_argument("youtube_playlist_url", type=str,
                            help='YouTube Playlist URL to extract playlist ID')

        # Optional Arguments
        parser.add_argument("-p", "--playlist_name", type=str, default="YouTube Playlist",
                            help='The name of the new Spotify playlist to be created (Default: YouTube Playlist)')
        parser.add_argument("-d", "--playlist_description", type=str, default="Songs from your Youtube playlist now "
                                                                              "on Spotify",
                            help='Description of the Spotify Playlist)')
        parser.add_argument("-a", "--playlist_privacy", type=bool, default=False,
                            help='The privacy of the playlist (Default: private)')

        return parser.parse_args()

    def extract_songs(self, _yt_playlist_url):
        """
        Extracts the title of the videos (songs) in the desired playlist and returns a list of the titles
        :param _yt_playlist_url:
        :return yt_song_list:
        """
        # Extract Playlist ID from Command Line YouTube URL Argument
        yt_playlist_id = _yt_playlist_url.split('=')

        # Retrieve Data from Youtube Playlist
        yt_query = "https://www.googleapis.com/youtube/v3/playlistItems"
        yt_request = {
            'key': f"{self.youtube_token}",
            'part': "snippet,contentDetails,id,status",
            'playlistId': f"{yt_playlist_id[1]}",
            'fields': "items/snippet(title)"
        }
        yt_response = requests.get(url=yt_query, params=yt_request)
        yt_response_mod = yt_response.json()
        yt_song_list = []
        # Add Playlist Video titles to an array
        for items in yt_response_mod["items"]:
            video_id = items["snippet"]["title"]
            yt_song_list.append(video_id)

        return yt_song_list

    def spotify_playlist(self, _playlist_name, _playlist_description, _playlist_privacy):
        """
        Creates a new Spotify Playlist under the appropriate user id and returns the playlist ID
        :param _playlist_name:
        :param _playlist_description:
        :param _playlist_privacy:
        :return playlist_id:
        """
        query = f"https://api.spotify.com/v1/users/{self.spotify_user_id}/playlists"

        request_body = json.dumps({
            "name": f"{_playlist_name}",
            "description": f"{_playlist_description}",
            "public": _playlist_privacy
        })

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_token}"
        }

        response = requests.post(url=query, data=request_body, headers=headers)
        response_mod = response.json()
        playlist_id = response_mod["id"]

        return playlist_id

    def spotify_song_search(self, _yt_song_list):
        """
        HTTP query request of the song titles in Spotify and adds the Spotify's song URI into a new list
        :param _yt_song_list:
        :return song_uri:
        """
        song_type = "track"
        song_market = "US"
        song_uri = []

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_token}"
        }
        for songs in _yt_song_list:
            get_song_query = f"https://api.spotify.com/v1/search?q={songs}&type={song_type}&market={song_market}&limit=1"
            get_song = requests.get(url=get_song_query, headers=headers)
            get_song_mod = get_song.json()
            song_id = get_song_mod["tracks"]["items"][0]["uri"]
            song_uri.append(song_id)

        return song_uri

    def add_to_playlist(self, _song_uri, _playlist_id):
        """
        Based on the param _song_uri, adds each item of that list into the desired playlist
        :param _song_uri:
        :param _plaulist_id:
        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_token}"
        }

        for i in _song_uri:
            track_query = f"https://api.spotify.com/v1/playlists/{_playlist_id}/tracks?uris={i.replace(':', '%3A')}"
            add_tracks = requests.post(url=track_query, headers=headers)


if __name__ == '__main__':
    playlist_converter = PlaylistConverter()

    # Defining the Command Line Arguments
    args = playlist_converter.setup_args()
    youtube_playlist = args.youtube_playlist_url
    playlist_name = args.playlist_name
    playlist_description = args.playlist_description
    playlist_privacy = args.playlist_privacy

    youtube_extract = playlist_converter.extract_songs(youtube_playlist)
    spotify_new_playlist = playlist_converter.spotify_playlist(playlist_name, playlist_description, playlist_privacy)
    songs_to_add = playlist_converter.spotify_song_search(youtube_extract)
    playlist_converter.add_to_playlist(songs_to_add, spotify_new_playlist)
