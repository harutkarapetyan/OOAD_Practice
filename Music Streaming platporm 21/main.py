from MusicStreamingPlatform import MusicStreamingPlatform


if __name__ == "__main__":
    music_platform = MusicStreamingPlatform()

    artist1 = music_platform.create_artist("Artist A", "artista@examplegmail.com")
    artist2 = music_platform.create_artist("Artist B", "artistb@examplegmail.com")

    song1 = music_platform.create_song("Rock Song 1", artist1, 240, "Rock")
    song2 = music_platform.create_song("Pop Song 1", artist2, 200, "Pop")

    user1 = music_platform.create_user("User 1", "user1@example.com")
    user2 = music_platform.create_user("User 2", "user2@example.com")

    user1.add_favorite_song(song1)
    user2.add_favorite_song(song2)

    found_songs = music_platform.search_songs("Rock")
    print("Found Songs:")
    for song in found_songs:
        print(song.title)

    print("Favorite Songs for User 1:")
    for song in user1.favorite_songs:
        print(song.title)

    print("Artists on the Platform:")
    artists = music_platform.discover_artists()
    for artist in artists:
        print(artist.name)


   
