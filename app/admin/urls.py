from . import admin

from views import hello_world


admin.add_url_rule('/', 'hello_world', hello_world, methods=['GET'])
