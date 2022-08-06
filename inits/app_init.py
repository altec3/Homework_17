from flask import Flask
from init.db_init import db

APP_CONFIG = "../configs/app_config.py"


def app_init(config_file: str = APP_CONFIG) -> Flask:

    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)

    return app
