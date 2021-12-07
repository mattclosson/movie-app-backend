"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "MovieController@index").name("index"),
        Get("/@id", "MovieController@show").name("show"),
        Post("/", "MovieController@create").name("create"),
        Put("/@id", "MovieController@update").name("update"),
        Delete("/@id", "MovieController@destroy").name("destroy")
    ], prefix="/movies", name="movies")
]
