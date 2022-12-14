import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'base.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
JSONIFY_PRETTYPRINT_REGULAR = True
RESTX_JSON = {'ensure_ascii': False}
DIRECTORS_DATA = "project/setup/fixtures/directors.json"
GENRES_DATA = "project/setup/fixtures/genres.json"
MOVIES_DATA = "project/setup/fixtures/movies.json"
POSTS_PER_PAGE = 10
