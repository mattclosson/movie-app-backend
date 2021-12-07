"""Movie Model."""

from masoniteorm.models import Model


class Movie(Model):
    __table__="movies"