import os
import sys
import re
import argparse
import pdb
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--target_dir', help='directory containing psx iso folders (i.e. from PSX2PSP)')
args = parser.parse_args()

psx_data_center_website = 'https://psxdatacenter.com/ntsc-u_list.html'
html = requests.get(psx_data_center_website)
soup = BeautifulSoup(html.text, 'html.parser')

target_dir = args.target_dir
psx_dirs = os.listdir(target_dir)

pdb.set_trace()
# col2 = serial num
# col3 = game name
for d in psx_dirs:
    matches = re.search(d, html.text)
    print(matches)
