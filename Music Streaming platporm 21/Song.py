from abc import ABC

class Song(ABC):
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

class RockSong(Song):
    def __init__(self, title, artist, duration):
        super().__init__(title, artist, duration, "Rock")

class PopSong(Song):
    def __init__(self, title, artist, duration):
        super().__init__(title, artist, duration, "Pop")
