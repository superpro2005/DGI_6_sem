class Song:
    def __init__(self, title, artist, release_year) -> None:
        self.title = title
        self.artist = artist
        self.release_year = release_year
some_song= Song('Какая-то песня', 'Кто-то', 2024)
print(some_song.get_info())
