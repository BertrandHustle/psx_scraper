# native
import argparse
import os
# project
import GamesList

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="directory to scrape")

args = parser.parse_args()
dir_to_scrape = os.pardir
if args.dir:
    dir_to_scrape = args.dir

folders = os.listdir(dir_to_scrape)

games_list = GamesList.GamesList()

urls = [
    'https://psxdatacenter.com/ulist.html',
    'https://psxdatacenter.com/plist.html',
    'https://psxdatacenter.com/jlist.html'
    ]

for url in urls:
    games_list.populate_games_list(url)

for folder in folders:
    lookup_result = games_list.get_name_by_part_number(folder)
    if lookup_result:
        os.rename(os.path.join(dir_to_scrape, folder), os.path.join(dir_to_scrape, lookup_result))
