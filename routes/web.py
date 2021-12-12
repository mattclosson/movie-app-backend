"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "MovieController@index").name("index"),
        Get("/@id", "MovieController@show").name("show"),
        Post("/", "MovieController@create").name("create"),
        Put("/@id", "MovieController@update").name("update"),
        Delete("/@id", "MovieController@destroy").name("destroy"),
        Get("/@id/reviews", "MovieController@get_movie_reviews").name("get_reviews")
    ], prefix="/movies", name="movies"),
    RouteGroup([ 
        Get("/", "ReviewController@index").name("index"),
        Post("/", "ReviewController@create").name("create"),
        Get("/@id", "ReviewController@show").name("show"),
        Put("/@id", "ReviewController@update").name("update"),
        Delete("/@id", "ReviewController@destroy").name("destroy")
    ], prefix="/reviews", name="reviews"),
]
