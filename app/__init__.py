from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin import Admin
import os

db = MongoEngine()
from app.models.models import ImportantDate

def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.path.join(app.root_path, '..', 'config', 'production.cfg')
    else:
        config = os.path.join(app.root_path, '..', 'config', config)

    app.config.from_pyfile(config)
    # db.init_app(app, config_prefix="MONGO_PSI")

    # app.config['SECRET_KEY'] = '123456790'
    # app.config['MONGODB_SETTINGS'] = {'DB': 'psi'}

    db.init_app(app)

    admin = Admin(app, name='PSI Admin Page')
    #TODO add more views
    admin.add_view(ModelView(ImportantDate))

    from main import main as site_blueprint
    app.register_blueprint(site_blueprint)

    # from admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
