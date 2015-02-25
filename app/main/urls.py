from . import main

from views import main as main_page


main.add_url_rule('/', 'main', main_page, methods=['GET'])
