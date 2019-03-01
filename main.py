import os
import sys
import urllib3
import re
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()

psx_data_center_website = 'https://psxdatacenter.com/ntsc-u_list.html'

target_dir = args.dir
psx_dirs = os.listdir(target_dir)
psx_dirs = psx_dirs.split(' ')
for d in psx_dirs:
    html_content = urllib2.urlopen(psx_data_center_website).read()
    matches = re.findall()
    print(matches)
