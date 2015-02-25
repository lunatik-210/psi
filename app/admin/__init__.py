from flask.ext.admin import Admin

admin = Admin(name="CMS PSI Admin Panel")

from . import urls
