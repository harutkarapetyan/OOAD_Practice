from Song import Song
from Album import Album
from Playlist import Playlist
from Music_Service import MusicService


if __name__ == "__main__":

    service = MusicService()

    # Create songs
    song1 = Song("Song 1", "Rihanna", 4.5)
    song2 = Song("Song 2", "Eminem", 4.2)
    song3 = Song("Song 3", "50 Cent", 3.1)

    # Create albums
    album1 = Album("Album 1", "Rihanna", "2023-01-15")
    album1.add_song(song1)
    album1.add_song(song3)

    # Create playlists
    playlist1 = Playlist("Song 1", "Rihanna")
    playlist1.add_song(song1)
    playlist1.add_song(song2)

    # Add items to the music service
    service.add_music_item(song1)
    service.add_music_item(song2)
    service.add_music_item(song3)
    service.add_music_item(album1)
    service.add_music_item(playlist1)

    # Search for songs and play them
    results = service.search("Eminem")
    for result in results:
        result.play()

