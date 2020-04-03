import requests
from bs4 import BeautifulSoup


class PartNumberFinder:
    # frameset rows -> frame src ulist.html -> #document -> html -> body -> table102 -> class=col2/3
    # soup("td")
    @staticmethod
    def get_game_names_and_part_numbers(url: str) -> list:
        """
        gets all psx games by name and part number from given url
        :param url: url to scrape from
        :return games: list of name, part_number tuples
        """
        spoofed_user = \
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'user-agent': spoofed_user}
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        tables = soup.find_all("tr")
        games = []
        for table in tables:
            cell = [cell.text for cell in table.find_all('td')]
            # if cell is empty
            if not cell:
                continue
            games.append((cell[1], cell[2].replace(u'\xa0', u' ')))
        return games


