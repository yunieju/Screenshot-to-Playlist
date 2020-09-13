# Sceenshot to Playlist
Extract songs from a screenshot image and generate a Spotify playlist

## Technologies 
- Spotify API
- Pytesseract library (Optical Character Recognition(OCR) tool)
- Requests library

## Setup
- install all dependencies
```
pip3 install -r requirements.txt
```
- Run the app
```
python run.py
```
- install Pytesseract package in your local machine

## Spotify API Token
- get your Spotify ID and OAuth Token and add id to spotify_auth.json in creds folder
- you can get your User ID from [Account Overview](https://www.spotify.com/us/account/overview/) in username
- You can get API Token in [Spotify Web API website](https://developer.spotify.com/console/post-playlists/)
- Note: need to re-generate the token every hour!

## ToDo 
- Test cases
- Error Handling
- Improvement on title and artist extraction
- Web application!


