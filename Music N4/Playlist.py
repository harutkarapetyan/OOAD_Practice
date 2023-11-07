from validate_decorators import validate_non_empty_string
from Song import MusicItem

class Playlist(MusicItem):
    @validate_non_empty_string("name")
    def __init__(self, title, name):
        super().__init__(title, "")
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        if len(self.songs) > 0:
            print(f"Now playing playlist: {self.title} - {self.name}")
            for song in self.songs:
                song.play()
        else:
            print(f"Playlist {self.title} - {self.name} is empty.")

    def __str__(self):
        return f"Playlist: {self.title} - {self.name}"
