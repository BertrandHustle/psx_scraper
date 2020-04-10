# native
import argparse
import os
# project
from psxDb import PsxDb

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="directory to scrape")

args = parser.parse_args()
dir_to_scrape = os.curdir
if args.dir:
    dir_to_scrape = args.dir

folders = os.listdir(dir_to_scrape)

psx_us = 'https://psxdatacenter.com/ulist.html'
psx_eu = 'https://psxdatacenter.com/plist.html'
psx_jp = 'https://psxdatacenter.com/jlist.html'

dbs = [
    PsxDb('psx_us', psx_us),
    PsxDb('psx_jp', psx_jp),
    PsxDb('psx_eu', psx_eu)
]

for db in dbs:
    for folder in folders:
        lookup_result = db.get_name_by_part_number(folder)
        if lookup_result:
            if dir_to_scrape == '.':
                os.rename(folder, lookup_result)
            else:
                os.rename(os.path.join(dir_to_scrape, folder), lookup_result)

