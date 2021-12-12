"""Review Migration."""

from masoniteorm.migrations import Migration


class Review(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("reviews") as table:
            table.increments("id")
            table.string("body")
            table.integer("rating")
            table.integer("movie_id")
            table.foreign("movie_id").references("id").on("movies")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("reviews")
