# project
from psx_db import PsxDb

psx_us = 'https://psxdatacenter.com/ulist.html'
psx_eu = 'https://psxdatacenter.com/plist.html'
psx_jp = 'https://psxdatacenter.com/jlist.html'

dbs = [
    PsxDb('psx_us', psx_us),
    PsxDb('psx_jp', psx_jp),
    PsxDb('psx_eu', psx_eu)
]

for db in dbs:
    print(db.get_name_by_part_number('SLUS-00975'))
