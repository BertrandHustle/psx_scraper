#! python
# native
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', help='directory to scrape')
parser.add_argument('-l', '--log', help='enables logging', action='store_true')

args = parser.parse_args()
dir_to_scrape = os.curdir
if args.dir:
    dir_to_scrape = args.dir

folders = [d for d in os.listdir(dir_to_scrape) if os.path.isdir(d)]
log_file = 'psx_scraper.log'
# 0 out log file if it exists
try:
    open(log_file, 'w').close()
except FileNotFoundError:
    pass


def get_game_name(filename):
    gamename = ''
    with open(filename, 'rb') as eboot:
        # check for PBP header
        if not eboot.read(4).decode() == '\x00' + 'PBP':
            return False
        else:
            eboot.seek(int('0x358', base=16))
            while True:
                gamename += eboot.read(1).decode()
                if gamename[-1:] == '\x00':
                    return gamename[:-1]


# TODO: add error/not found logging
# TODO: restrict game name + path to 31 chars
for folder in folders:
    folder_path = os.path.join(dir_to_scrape, folder)
    eboot_path = os.path.join(folder_path, 'EBOOT.PBP')
    contains_eboot = 'EBOOT.PBP' in os.listdir(folder_path)
    new_folder_name = ''
    if contains_eboot:
        new_folder_name = get_game_name(eboot_path)
        if new_folder_name:
            new_folder_path = os.path.join(dir_to_scrape, new_folder_name)
            os.rename(folder_path, new_folder_path)
        else:
            pass
    elif args.log:
        with open(log_file, 'a') as log:
            if not contains_eboot:
                log.write('NO EBOOT.PBP FILE FOUND IN: ' + folder_path + '\n')
            else:
                log.write('GAME NAME NOT FOUND: ' + eboot_path + '\n')
    else:
        pass
