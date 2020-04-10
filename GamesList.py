# project
from PartNumberFinder import PartNumberFinder


class GamesList:
    """
    tools for building dict of game name/part_number pairs
    """
    def __init__(self):
        self.games_list = {}

    def populate_games_list(self, url):
        """
        Populates dict with games by name and part number
        :return: None
        """
        for pair in PartNumberFinder.get_game_names_and_part_numbers(url):
            self.games_list[pair[0]] = pair[1]

    def get_name_by_part_number(self, part_number: str) -> str:
        """
        gets game name given a part number
        :return str: name
        """
        try:
            return self.games_list[part_number]
        # TODO: have this output to log
        except KeyError:
            pass

