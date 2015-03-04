from app import login_manager
from app.models import User


def user_loader(user_name):
    return User.objects(user_name=user_name).first()

login_manager.user_loader(user_loader)
