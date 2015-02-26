from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.login import current_user


class BaseModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()	


class ImportantDateView(BaseModelView):
	pass


class VideoView(BaseModelView):
	pass