#native
import re
import os
import sys
sys.path.append(os.pardir)
#project
import PartNumberFinder


def test_get_game_names_and_part_numbers():
    test_game_list = PartNumberFinder.PartNumberFinder.get_game_names_and_part_numbers('https://psxdatacenter.com/ulist.html')
    for g in test_game_list:
        number = g[0]
        name = g[1]
        assert type(name) == str
        assert re.match(r'[A-Z]{4}-\d{5}|[A-Z]{3}-\d{6}|[A-Z]{4}-\dXXXX', number)