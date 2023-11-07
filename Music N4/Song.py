from validate_decorators import validate_non_empty_string, validate_positive_number
from abc import ABC, abstractmethod

class MusicItem(ABC):
    @validate_non_empty_string("title")
    @validate_non_empty_string("artist")
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    @abstractmethod
    def play(self):
        pass

class Song(MusicItem):
    def __init__(self, title, artist, length):
        super().__init__(title, artist)
        self.length = length

    def play(self):
        print(f"Now playing: {self.title} by {self.artist}")

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.length} minutes)"


