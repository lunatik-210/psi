from flask.ext.admin import Admin

from app.admin.views import DefaultLoginView


admin = Admin(name="CMS PSI Admin Panel", index_view=DefaultLoginView())

from . import urls
