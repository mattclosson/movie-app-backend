"""Movie Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Movie(Model):
    __table__="movies"

    __fillable__ = ["title", "description", "year", "poster"]
    @has_many("id", "movie_id")
    def reviews(self):
        from app.Review import Review
        return Review