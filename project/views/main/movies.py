from flask import request, current_app as app
from flask_restx import Resource, Namespace

from project.setup.schemas.schema import MovieSchema
from project.setup.inits.app_init import api, db
from project.setup.models.models import Director, Genre, Movie
from project.utils.models_converter import convert_and_register_model

movies_ns: Namespace = Namespace("movies")

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

convert_and_register_model("movie", movie_schema)
convert_and_register_model("movies", movies_schema)


@movies_ns.route("/")
class MoviesView(Resource):

    @movies_ns.response(200, description="Возвращает список фильмов", model=api.models["movies"])
    def get(self):

        page = request.args.get("page", 1, type=int)
        db_request = db.session.query(Movie)

        if request.args.get("director_id"):
            did = int(request.args.get("director_id"))
            db_request = db_request.filter(Movie.director_id == did)

        if request.args.get("genre_id"):
            gid = int(request.args.get("genre_id"))
            db_request = db_request.filter(Movie.genre_id == gid)

        all_movies = db_request.paginate(page=page, per_page=app.config.get("POSTS_PER_PAGE"), error_out=False).items
        return movies_schema.dump(all_movies), 200

    @movies_ns.expect(api.models["movie"])
    @movies_ns.response(201, description="Фильм успешно добавлен в фильмотеку")
    @movies_ns.response(404, description="Ошибка добавления фильма в фильмотеку")
    def post(self):
        try:
            movie: dict = movie_schema.load(request.json)
            with db.session.begin():
                db.session.add(Movie(**movie))
        except Exception:
            return "", 400
        else:
            return "", 201

@movies_ns.route("/<int:mid>")
class MovieView(Resource):

    @movies_ns.response(200, description="Возвращает фильм по его ID", model=api.models["movie"])
    @movies_ns.response(404, description="Фильм с данным ID не найден в фильмотеке")
    def get(self, mid: int):
        movie = db.session.query(Movie).get_or_404(mid)
        return movie_schema.dump(movie), 200

    @movies_ns.response(204, description="Данные по фильму успешно обновлены")
    @movies_ns.response(404, description="Ошибка обновления данных фильма")
    def put(self, mid: int):
        with db.session.begin():
            if db.session.query(Movie).filter(Movie.id == mid).update(request.json):
                return "", 204
        return "", 404

    @movies_ns.response(204, description="Фильм успешно удален из фильмотеки")
    @movies_ns.response(404, description="Фильм с данным ID не найден в фильмотеке")
    def delete(self, mid: int):
        with db.session.begin():
            if db.session.query(Movie).filter(Movie.id == mid).delete():
                return "", 204
        return "", 404
