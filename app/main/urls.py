from . import main

from views import main as main_page
from views import video as video_page


main.add_url_rule('/', 'main', main_page, methods=['GET'])
main.add_url_rule('/video', 'video', video_page, methods=['GET'])
