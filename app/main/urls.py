from . import main

from views import main as main_page
from views import video as video_page
from views import pictures as pictures_page
from views import images as images_endpoint
from views import speakers as speakers_page
from views import menu as menu_page
from views import registration as registration_page


main.add_url_rule('/', 'main', main_page, methods=['GET'])
main.add_url_rule('/video', 'video', video_page, methods=['GET'])
main.add_url_rule('/pictures', 'pictures', pictures_page, methods=['GET'])
main.add_url_rule('/speakers', 'speakers', speakers_page, methods=['GET'])
main.add_url_rule('/registration', 'registration', registration_page, methods=['GET'])
main.add_url_rule('/images/<path:filename>', 'images', images_endpoint, methods=['GET'])
main.add_url_rule('/menu', 'menu', menu_page, methods=['GET'])
