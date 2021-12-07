""" A MovieController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Movie import Movie

class MovieController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", MovieController)
        """
        id = self.request.param("id")
        return Movie.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return Movie.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", MovieController)
        """
        title = self.request.input("title")
        description = self.request.input("description")
        poster = self.request.input("poster")
        year = self.request.input("year")
        movie = Movie.create({"title": title, "description": description, "poster": poster, "year": year})
        return movie


    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", MovieController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", MovieController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", MovieController)
        """
        title = self.request.input("title")
        description = self.request.input("description")
        poster = self.request.input("poster")
        year = self.request.input("year")
        id = self.request.param("id")
        Movie.where("id", id).update({"title": title, "description": description, "poster": poster, "year": year})
        return Movie.where("id", id).get()


    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", MovieController)
        """
        id = self.request.param("id")
        movie = Movie.where("id", id).get()
        Movie.where("id", id).delete()
        return movie 