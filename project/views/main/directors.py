from flask import request
from flask_restx import Resource, Namespace

from project.setup.schemas.schema import DirectorSchema
from project.setup.inits.app_init import api
from project.setup.inits.db_init import db
from project.setup.models.models import Director
from project.utils.models_converter import convert_and_register_model

directors_ns: Namespace = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

convert_and_register_model("director", director_schema)
convert_and_register_model("directors", directors_schema)


@directors_ns.route("/")
class DirectorsView(Resource):

    @directors_ns.response(200, description="Возвращает список режиссеров", model=api.models["directors"])
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200

    @directors_ns.expect(api.models["director"])
    @directors_ns.response(201, description="Режиссер успешно добавлен в список")
    @directors_ns.response(404, description="Ошибка добавления режиссера в список")
    def post(self):
        try:
            director: dict = director_schema.load(request.json)
            with db.session.begin():
                db.session.add(Director(**director))
        except Exception:
            return "", 400
        else:
            return "", 201


@directors_ns.route("/<int:did>")
class DirectorView(Resource):

    @directors_ns.response(200, description="Возвращает режиссера по его ID", model=api.models["director"])
    @directors_ns.response(404, description="Режиссер с данным ID не найден в базе")
    def get(self, did: int):
        director = db.session.query(Director).get_or_404(did)
        return director_schema.dump(director), 200

    @directors_ns.response(204, description="Данные по режиссеру успешно обновлены")
    @directors_ns.response(404, description="Ошибка обновления данных режиссера")
    def put(self, did: int):
        with db.session.begin():
            if db.session.query(Director).filter(Director.id == did).update(request.json):
                return "", 204
        return "", 404

    @directors_ns.response(204, description="Режиссер успешно удален из базы")
    @directors_ns.response(404, description="Режиссер с данным ID не найден в базе")
    def delete(self, did: int):
        with db.session.begin():
            if db.session.query(Director).filter(Director.id == did).delete():
                return "", 204
        return "", 404
