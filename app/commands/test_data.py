from . import test_data
from app.models.models import User


@test_data.command
def create():
    "Fill database with test data"
    user = User(user_name="admin", password="admin")
    user.save()


@test_data.command
def delete():
    "Delete all data from database"
    User.drop_collection()


@test_data.command
def recreate():
    "Delete all data from database and then fill it again"
    delete()
    create()
