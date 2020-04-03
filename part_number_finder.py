import requests
from bs4 import BeautifulSoup

psx_website_us = 'https://psxdatacenter.com/ulist.html'
psx_website_eu = 'https://psxdatacenter.com/plist.html'
psx_website_jp = 'https://psxdatacenter.com/jlist.html'

class PartNumberFinder:

    # frameset rows -> frame src ulist.html -> #document -> html -> body -> table102 -> class=col2/3
    # soup("td")
    @staticmethod
    def get_game_name_from_part_number(part_number: str):
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        html = requests.get(psx_data_center_website, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        tables = soup.find_all("tr")
        for table in tables:
            cell = [cell.text for cell in table.find_all('td')]
            # if cell is empty
            if not cell:
                continue
            game_id = cell[1]
            game_name = cell[2]
            print(game_id, game_name)

