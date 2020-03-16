import requests
from bs4 import BeautifulSoup

psx_data_center_website = 'https://psxdatacenter.com/ntsc-u_list.html'


class PartNumberFinder:

    # frameset rows -> frame src ulist.html -> #document -> html -> body -> table102 -> class=col2/3
    @staticmethod
    def get_game_name_from_part_number(part_number: str):
        html = requests.get(psx_data_center_website)
        soup = BeautifulSoup(html.text, 'html.parser')
        print('test')

