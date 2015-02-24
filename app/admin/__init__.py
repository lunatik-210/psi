from flask import Blueprint

admin = Blueprint('login', __name__)

from . import urls
