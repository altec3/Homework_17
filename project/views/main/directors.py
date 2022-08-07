from flask import request
from flask_restx import Resource, Namespace

from project.setup.schemas.schema import DirectorSchema
from project.setup.inits.app_init import db
from project.setup.inits.app_init import api
from project.setup.models.models import Director

directors_ns: Namespace = api.namespace("directors")

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200

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

    def get(self, did: int):
        director = db.session.query(Director).get(did)
        if director is None:
            return "", 404
        else:
            return director_schema.dump(director), 200

    def put(self, did: int):
        with db.session.begin():
            if db.session.query(Director).filter(Director.id == did).update(request.json):
                return "", 204
        return "", 404

    def delete(self, did: int):
        with db.session.begin():
            if db.session.query(Director).filter(Director.id == did).delete():
                return "", 204
        return "", 404
