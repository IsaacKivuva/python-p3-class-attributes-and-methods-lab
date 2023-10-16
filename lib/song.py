class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1 

    @classmethod
    def add_to_genres(cls,genre):
        if genre in cls.genres:
            cls.add_to_genre_count(genre)
        else:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls,artist):
        if artist in cls.artists:
            cls.add_to_artist_count(artist)
        else:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] += 1