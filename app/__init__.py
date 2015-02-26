from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

import os

db = MongoEngine()
login_manager = LoginManager()

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

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/admin/auth')

    from admin import admin as admin_panel
    admin_panel.init_app(app)

    return app
