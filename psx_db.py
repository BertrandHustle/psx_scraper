# native
import sqlite3
# project
from part_number_finder import PartNumberFinder


class PsxDb:
    """
    sqlite3 builder for psx game id/game name pairs
    :poram db_name: filename of database to create
    """
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect('databases/' + db_name + '.db')
        self.cursor = self.conn.cursor()
        # Create table
        self.cursor.execute('CREATE TABLE IF NOT EXISTS games(part_number text, name text)')
        self.conn.commit()

    def populate_games(self, url):
        """
        Populates database with games by name and part number
        :return: None
        """
        psx_pairs = PartNumberFinder.get_game_names_and_part_numbers(url)
        self.cursor.executemany('INSERT INTO games VALUES (?,?)', psx_pairs)
        # save changes to db
        self.conn.commit()

    def get_all_games(self):
        self.cursor.execute('SELECT * FROM games')
        print(self.cursor.fetchall())
