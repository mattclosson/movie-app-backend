""" A ReviewController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Review import Review

class ReviewController(Controller):
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
        return Review.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return Review.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", MovieController)
        """
        body = self.request.input("body")
        rating = self.request.input("rating")
        movie_id = self.request.input("movie_id")
        review = Review.create(body=body, rating=rating, movie_id=movie_id)
        return review

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", MovieController)
        """
        body = self.request.input("body")
        rating = self.request.input("rating")
        movie_id = self.request.input("movie_id")
        Review.where("id", id).update(body=body, rating=rating, movie_id=movie_id)
        return Review.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", MovieController)
        """
        id = self.request.param("id")
        review = Review.where("id", id).get()
        Review.where("id", id).delete()
        return review 