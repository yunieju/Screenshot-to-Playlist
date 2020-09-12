import os
import json

from read_text_file import ReadText
from spotify_client import SpotifyClient
from image_converter import ImgConverter


def run():
    with open('creds/spotify_auth.json') as sp:
        data = sp.read()
    spotify_cred = json.loads(data)

    image_converter = ImgConverter()
    read_text_file = ReadText()
    spotify_client = SpotifyClient(spotify_cred["spotify_token"])

    img_location = input("Enter location of image file: ")
    txt_file = "sample.txt" # make a dump file
    txt_location = image_converter.extract_text(img_location, txt_file)
    playlist_name = input("Enter a name for your new playlist: ")
    playlist_id = spotify_client.create_new_playlist(playlist_name)

    songs_arr = read_text_file.read_txt(txt_location)
    songs = read_text_file.find_artist_track(songs_arr)
    print(songs)
    print(f"Attept to add {len(songs)} songs")

    uris = []
    for song in songs:
        spotify_song_uri = spotify_client.search_song(song.artist, song.track)
        if spotify_song_uri:
            uris.append(spotify_song_uri)
        added_song = spotify_client.add_song_to_spotify(uris, playlist_id)
    print(f"Successfully added songs in your {playlist_name} playlist")


if __name__ == '__main__':
    run()
