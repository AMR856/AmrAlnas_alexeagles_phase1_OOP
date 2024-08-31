#!/usr/bin/env python3

class Movie:
    def __init__(self,
                title: str,
                director: str,
                release_year: str,
                genre: str,
                rating: float) -> None:
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.rating = rating

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if isinstance(value, str):
            self.__title = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, value: str) -> None:
        if isinstance(value, str):
            self.__director = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, value: int) -> None:
        if isinstance(value, int):
            self.__release_year = value
        else:
            raise TypeError('You have to provide an integer')

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, value: str) -> None:
        if isinstance(value, str):
            self.__genre = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, value: float) -> None:
        if isinstance(value, float):
            self.__rating = value
        else:
            raise TypeError('You have to provide a float')

    def __str__(self) -> str:
        return f"Movie's title is {self.title}\nIts director is {self.director}\nRelease Year is {self.release_year}\nGenre is {self.genre}\nAnd its Rating is {self.rating}"