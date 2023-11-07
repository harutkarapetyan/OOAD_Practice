from validate_decorators import validate_non_empty_string
class MusicService:
    def __init__(self):
        self.music_library = []

    def add_music_item(self, item):
        self.music_library.append(item)

    def search(self, keyword):
        results = []
        for item in self.music_library:
            if keyword.lower() in item.title.lower() or keyword.lower() in item.artist.lower():
                results.append(item)
        return results
