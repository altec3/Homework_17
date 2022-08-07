from flask import Flask

from project.setup.inits.api_init import api
from project.setup.inits.db_init import db
from project.utils.db_tools import DBTools
from project.utils.json_tools import JSONTools
from project.setup.models.models import Director, Genre, Movie


APP_CONFIG = "../configs/app_config.py"


def app_init(config_file: str = APP_CONFIG) -> Flask:

    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    api.init_app(app)

    # Импортируем маршруты
    from project.views.main import movies, directors, genres  # noqa

    db_tools = DBTools()
    json_tools = JSONTools()

    with app.app_context():
        # Создаем базу. Добавляем таблицы в базу
        db.drop_all()
        db.create_all()

        # Заполняем таблицы в базе
        directors_data = json_tools.load_json(app.config.get("DIRECTORS_DATA"))
        genres_data = json_tools.load_json(app.config.get("GENRES_DATA"))
        movies_data = json_tools.load_json(app.config.get("MOVIES_DATA"))
        db_tools.insert_data(Director, directors_data)
        db_tools.insert_data(Genre, genres_data)
        db_tools.insert_data(Movie, movies_data)

    return app
