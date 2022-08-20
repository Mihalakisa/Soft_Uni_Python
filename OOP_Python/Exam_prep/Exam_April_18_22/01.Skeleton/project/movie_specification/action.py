from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    DEFAULT_AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.DEFAULT_AGE_RESTRICTION:
            raise ValueError(f'Action movies must be restricted for audience'
                             f' under {self.DEFAULT_AGE_RESTRICTION} years!')
        self.__age_restriction = value
