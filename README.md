# Playlist-Converter

Convert any YouTube music playlist (either yours or a public one) into a new Spotify playlist with the use of the [Spotify API](https://developer.spotify.com/ "Spotify API title") and the [YouTube API](https://developers.google.com/youtube/ "YouTube API title"). 

## Set-Up ## 
* Install all dependencies found in main.py script 
* Load in all required fields in secret.py script 

## Execution ## 

To run the app, there is one required argument which is the URL to the YouTube playlist in which you want to convert. Sample execution below: 

`python main.py "https://www.youtube.com/playlist?list=PLL4EGPlAvNxCEOa0KKKxJ50KXocCTasyp"`

To further customize the playlist being created, there are three optional arguments (playlist_name (str), playlist_description (str), playlist_privacy (bool)) in which you can change. The default values for these arguments can be found in main.py. Sample execution below: 

`python main.py "https://www.youtube.com/playlist?list=PLL4EGPlAvNxCEOa0KKKxJ50KXocCTasyp" -p="My Playlist" -d="Playlist from YouTube" -a=True`

## Future Improvements ## 
- [ ] Add error handling 
- [ ] Improve UI (create GUI or webpage)
- [ ] OAuth Token Regenerator (Spotify)
- [ ] Extend to more services (Apple Music, Google Music, etc) 
- [ ] Allow users to pick which two services to convert from and to 
