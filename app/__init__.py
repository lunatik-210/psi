from flask import Flask
from flask.ext.pymongo import PyMongo

import os

db = PyMongo()

def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.path.join(app.root_path, '..', 'config', 'production.cfg')
    else:
        config = os.path.join(app.root_path, '..', 'config', config)

    app.config.from_pyfile(config)

    db.init_app(app, config_prefix="MONGO_PSI")

    from main import main as site_blueprint
    app.register_blueprint(site_blueprint)

    from admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
