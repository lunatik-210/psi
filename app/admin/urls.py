from . import admin

from views import login, logout

admin.add_url_rule('/login', 'login', login, methods=['GET','POST'])
admin.add_url_rule('/logout', 'logout', logout, methods=['GET'])
