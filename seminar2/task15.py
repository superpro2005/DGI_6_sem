class Audio_Item:
    def __init__(self, title, artist) -> None:
        self.title = title
        self.artist = artist


class Song(Audio_Item):
    def __init__(self, title, artist, release_year) -> None:
        super().__init__(title, artist)
        self.release_year = release_year

    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info


class Podcast_Episode(Audio_Item):
    def __init__(self, title, artist, duration, guest) -> None:
        super().__init__(title, artist)
        self.duration = duration
        self.guest = guest
        self.over_30_min = self.check_is_over_30_min(duration)

    def check_is_over_30_min(self, duration):
        return (duration > 1800)

    def __str__(self) -> str:
        string_info = str(self.__dict__)
        return string_info


some_song = Song('Какая-то песня', 'Кто-то', 2024)
print(some_song)
some_podcast = Podcast_Episode('Какой-то подкаст', 'Кто-то', 123456, 'Кто-то другой')
print(some_podcast)