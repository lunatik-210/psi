from . import main

from views import main as main_page
from views import video as video_page
from views import pictures as pictures_page
from views import images as images_endpoint


main.add_url_rule('/', 'main', main_page, methods=['GET'])
main.add_url_rule('/video', 'video', video_page, methods=['GET'])
main.add_url_rule('/pictures', 'pictures', pictures_page, methods=['GET'])
main.add_url_rule('/images/<path:filename>', 'images', images_endpoint, methods=['GET'])
