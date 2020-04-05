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

for db in dbs:
    print(db.lookup_by_part_number_or_name('SLUS-00975'))
