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
        movie_id = self.request.input("movie_id")
        review = Review.create(body=body, movie_id=movie_id)
        return review
