# native
import argparse
import os
# project
from psxDb import PsxDb

psx_us = 'https://psxdatacenter.com/ulist.html'
psx_eu = 'https://psxdatacenter.com/plist.html'
psx_jp = 'https://psxdatacenter.com/jlist.html'

dbs = [
    PsxDb('psx_us', psx_us),
    PsxDb('psx_jp', psx_jp),
    PsxDb('psx_eu', psx_eu)
]

#parser = argparse.ArgumentParser()
#args = parser.parse_args()
#target_dir = args.dir
psx_dirs = os.listdir()
# psx_dirs = psx_dirs.split(' ')
for dir in psx_dirs:
    for db in dbs:
        lookup = db.lookup_by_part_number_or_name(dir)
        if lookup:
            os.rename(dir, lookup)

