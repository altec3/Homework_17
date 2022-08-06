from flask import request
from flask_restx import Resource, Namespace
from schemas.schema import MovieSchema

from inits.db_init import db
from inits.app_init import api
from models.models import Movie

movies_ns: Namespace = api.namespace("movies")

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):

        db_request = db.session.query(Movie)

        if request.args.get("director_id"):
            did = int(request.args.get("director_id"))
            db_request = db_request.filter(Movie.director_id == did)

        if request.args.get("genre_id"):
            gid = int(request.args.get("genre_id"))
            db_request = db_request.filter(Movie.genre_id == gid)

        all_movies = db_request.all()
        return movies_schema.dump(all_movies), 200


@movies_ns.route("/<int:mid>")
class MovieView(Resource):

    def get(self, mid):
        movie = db.session.query(Movie).get(mid)
        if movie is None:
            return {}, 404
        else:
            return movie_schema.dump(movie), 200
