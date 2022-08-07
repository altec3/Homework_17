from flask import request
from flask_restx import Resource, Namespace

from project.setup.schemas.schema import GenreSchema
from project.setup.inits.app_init import db
from project.setup.inits.app_init import api
from project.setup.models.models import Genre

genres_ns: Namespace = api.namespace("genres")

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        try:
            genre: dict = genre_schema.load(request.json)
            with db.session.begin():
                db.session.add(Genre(**genre))
        except Exception:
            return "", 400
        else:
            return "", 201


@genres_ns.route("/<int:gid>")
class GenreView(Resource):

    def get(self, gid: int):
        genre = db.session.query(Genre).get(gid)
        if genre is None:
            return "", 404
        else:
            return genre_schema.dump(genre), 200

    def put(self, gid: int):
        with db.session.begin():
            if db.session.query(Genre).filter(Genre.id == gid).update(request.json):
                return "", 204
        return "", 404

    def delete(self, gid: int):
        with db.session.begin():
            if db.session.query(Genre).filter(Genre.id == gid).delete():
                return "", 204
        return "", 404
