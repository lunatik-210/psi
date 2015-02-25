from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import urls

from .views import user_loader
from app import login_manager

login_manager.user_loader(user_loader)
