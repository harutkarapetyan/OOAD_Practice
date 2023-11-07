from abc import ABC
from User import User 
from Artist import Artist
from Song import Song

class MusicStreamingPlatform(ABC):
    def __init__(self):
        self.songs = []
        self.artists = []
        self.users = []

    def create_user(self, name, contact_info):
        user = User(name, contact_info)
        self.users.append(user)
        return user

    def create_artist(self, name, contact_info):
        artist = Artist(name, contact_info)
        self.artists.append(artist)
        return artist

    def create_song(self, title, artist, duration, genre):
        song = Song(title, artist, duration, genre)
        self.songs.append(song)
        return song

    def search_songs(self, keyword):
        found_songs = [song for song in self.songs if keyword.lower() in song.title.lower()]
        return found_songs

    def discover_artists(self):
        return self.artists