from . import test_data
from app.models.models import User, Video


@test_data.command
def create():
    "Fill database with test data"
    user = User(user_name="admin", password="admin")
    user.save()

    videos = ['qbWUXNPf65A', 'cBsMCDgd3lg', 'KoyA0PStmls', 'AjfejT2DrJo', '0WQTgIC1Pfs', '0WQTgIC1Pfs']

    for v in videos:
        video = Video(path=v)
        video.save()


@test_data.command
def delete():
    "Delete all data from database"
    User.drop_collection()
    save.drop_collection()


@test_data.command
def recreate():
    "Delete all data from database and then fill it again"
    delete()
    create()
