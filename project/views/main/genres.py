from flask import request
from flask_restx import Resource, Namespace

from project.setup.schemas.schema import GenreSchema
from project.setup.inits.app_init import api
from project.setup.inits.db_init import db
from project.setup.models.models import Genre
from project.utils.models_converter import convert_and_register_model

genres_ns: Namespace = Namespace("genres")

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

convert_and_register_model("genre", genre_schema)
convert_and_register_model("genres", genres_schema)


@genres_ns.route("/")
class GenresView(Resource):

    @genres_ns.response(200, description="Возвращает список жанров", model=api.models["genres"])
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200

    @genres_ns.expect(api.models["genre"])
    @genres_ns.response(201, description="Жанр успешно добавлен в базу")
    @genres_ns.response(404, description="Ошибка добавления жанра в базу")
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

    @genres_ns.response(200, description="Возвращает жанр по его ID", model=api.models["genre"])
    @genres_ns.response(404, description="Жанр с данным ID не найден в базе")
    def get(self, gid: int):
        genre = db.session.query(Genre).get_or_404(gid)
        return genre_schema.dump(genre), 200

    @genres_ns.response(204, description="Информация о жанре успешно обновлена")
    @genres_ns.response(404, description="Ошибка обновления информации о жанре")
    def put(self, gid: int):
        with db.session.begin():
            if db.session.query(Genre).filter(Genre.id == gid).update(request.json):
                return "", 204
        return "", 404

    @genres_ns.response(204, description="Жанр успешно удален из базы")
    @genres_ns.response(404, description="Жанр с данным ID не найден в базе")
    def delete(self, gid: int):
        with db.session.begin():
            if db.session.query(Genre).filter(Genre.id == gid).delete():
                return "", 204
        return "", 404
