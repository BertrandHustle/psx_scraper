# project
from psx_db import PsxDb

psx_website_us = 'https://psxdatacenter.com/ulist.html'
psx_website_eu = 'https://psxdatacenter.com/plist.html'
psx_website_jp = 'https://psxdatacenter.com/jlist.html'

urls = [psx_website_eu, psx_website_jp, psx_website_us]
db = PsxDb('psx_us')
db.populate_games(psx_website_us)
db.get_all_games()