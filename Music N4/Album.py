from validate_decorators import validate_positive_number
from Song import MusicItem


class Album(MusicItem):
    def __init__(self, title, artist, release_date):
        super().__init__(title, artist)
        self.release_date = release_date
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        if len(self.songs) > 0:
            print(f"Now playing album: {self.title} by {self.artist}")
            for song in self.songs:
                song.play()
        else:
            print(f"Album {self.title} by {self.artist} is empty.")

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.release_date})"
