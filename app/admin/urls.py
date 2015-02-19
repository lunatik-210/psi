from . import admin

from views import hello_world, login


admin.add_url_rule('/', 'hello_world', hello_world, methods=['GET'])
admin.add_url_rule('/login', 'login', login, methods=['GET'])
