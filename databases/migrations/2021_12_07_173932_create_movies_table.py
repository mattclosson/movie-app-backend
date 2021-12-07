"""CreateMoviesTable Migration."""

from masoniteorm.migrations import Migration


class CreateMoviesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("movies") as table:
            table.increments("id")
            table.string("title")
            table.string("description")
            table.string("year")
            table.string("poster")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("movies")
