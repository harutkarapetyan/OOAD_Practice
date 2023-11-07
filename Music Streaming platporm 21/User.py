from validate_decorators import validate_email, validate_non_empty_string

class User:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.favorite_songs = []
        self.favorite_artists = []

    def add_favorite_song(self, song):
        self.favorite_songs.append(song)

    def add_favorite_artist(self, artist):
        self.favorite_artists.append(artist)
