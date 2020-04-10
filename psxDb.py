# native
import sqlite3
from re import match
# project
from partNumberFinder import PartNumberFinder


class PsxDb:
    """
    sqlite3 builder for psx game id/game name pairs
    :poram db_name: filename of database to create
    :param url: url to scrape for data
    """
    def __init__(self, db_name: str, url: str):
        self.url = url
        self.conn = sqlite3.connect('databases/' + db_name + '.db')
        self.cursor = self.conn.cursor()
        # Create table
        self.cursor.execute('CREATE TABLE IF NOT EXISTS games(part_number text, name text)')
        # Check if table is already populated
        if self.cursor.execute("SELECT count(*) FROM games").fetchone()[0] < 0:
            self.populate_games()
        self.conn.commit()

    class PsxDbError(Exception):
        pass

    def populate_games(self):
        """
        Populates database with games by name and part number
        :return: None
        """
        psx_pairs = PartNumberFinder.get_game_names_and_part_numbers(self.url)
        self.cursor.executemany('INSERT INTO games VALUES (?,?)', psx_pairs)
        # save changes to db
        self.conn.commit()

    def get_name_by_part_number(self, part_number: str) -> str:
        """
        gets game name given a part number
        :return str: name
        """
        self.cursor.execute('SELECT * FROM games WHERE part_number=?', (part_number,))
        result = self.cursor.fetchone()
        if result:
            return result[1]

    def get_part_number_by_name(self, name: str) -> str:
        """
        looks up name by part number or vice verse
        :param target: either a part number or game name
        :return: part_number or name, depending on target
        """
        self.cursor.execute('SELECT * FROM games WHERE name=?', (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]


