from . import main

from api_methods import *

main.add_url_rule('/add_important_date', 'add_important_date', add_important_date, methods=['POST'])
main.add_url_rule('/fetch_all_dates', 'fetch_all_dates', fetch_all_dates, methods=['GET'])
main.add_url_rule('/fetch_dates_range', 'fetch_dates_range', fetch_dates_range, methods=['GET'])
