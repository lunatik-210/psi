from . import main

from views import hello_world


main.add_url_rule('/', 'hello_world', hello_world, methods=['GET'])
