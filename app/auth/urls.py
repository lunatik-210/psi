from . import auth

from views import login, logout

auth.add_url_rule('/login', 'login', login, methods=['GET','POST'])
auth.add_url_rule('/logout', 'logout', logout, methods=['GET'])
