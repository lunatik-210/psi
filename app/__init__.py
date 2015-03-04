import os

from flask import Flask, request
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.babelex import Babel
from app import constants
from app.languages import LANGUAGES

db = MongoEngine()
login_manager = LoginManager()
babel = Babel()


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.path.join(app.root_path, '..', 'config', 'production.cfg')
    else:
        config = os.path.join(app.root_path, '..', 'config', config)

    app.config.from_pyfile(config)

    db.init_app(app)
    login_manager.init_app(app)

    from main import main as site_blueprint
    app.register_blueprint(site_blueprint)

    from admin import admin as admin_panel
    admin_panel.init_app(app)

    # localization
    babel.init_app(app)
    return app


@babel.localeselector
def get_locale():
    return request.cookies.get(constants.LOCALE_TOKEN) or constants.DEFAULT_LOCALE
    # return request.accept_languages.best_match(LANGUAGES.keys())

# @babel.timezoneselector
# def get_timezone():
#     pass