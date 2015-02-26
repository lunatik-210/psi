from . import test_data
from app.models.models import User, Video, NewsItem, ImportantDate

@test_data.command
def create():
    "Fill database with test data"
    user = User(user_name="admin", password="admin")
    user.save()

    videos = ['qbWUXNPf65A', 'cBsMCDgd3lg', 'KoyA0PStmls', 'AjfejT2DrJo', '0WQTgIC1Pfs', '0WQTgIC1Pfs']

    for v in videos:
        video = Video(path=v)
        video.save()

    news = ["The PSI'14 is open. Congratulations to the Conference participants and organizers! See some photographs taken at the opening.",
    "The Programme of Workshop on Science Intensive Applied Software is available in PDF (in Russian).",
    "The Programme of Workshop 'Educational Informatics' is available in PDF.",
    "Registration for the conference begins at 8.00 am June 24 at New Peterhof Hotel."]

    for n in news:
        newsItem = NewsItem(content=n)
        newsItem.save()

    dates = ["abstract submission", "submission deadline", "notification of acceptance",
    "camera ready papers for pre-proceedings", "the conference dates", "camera ready papers due"]

    for d in dates:
        date = ImportantDate(description=d)
        date.save()


@test_data.command
def delete():
    "Delete all data from database"
    User.drop_collection()
    Video.drop_collection()
    NewsItem.drop_collection()
    ImportantDate.drop_collection()


@test_data.command
def recreate():
    "Delete all data from database and then fill it again"
    delete()
    create()
