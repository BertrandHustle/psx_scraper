# native
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="directory to scrape")

args = parser.parse_args()
dir_to_scrape = os.curdir
if args.dir:
    dir_to_scrape = args.dir

folders = [d for d in os.listdir(dir_to_scrape) if os.path.isdir(d)]


def get_game_name(filename):
    gamename = ''
    with open(filename, 'rb') as eboot:
        eboot.seek(int('0x358', base=16))
        while True:
            try:
                gamename += eboot.read(1).decode()
            except UnicodeDecodeError:
                return gamename.replace(' ', '')


for folder in folders:
    folder_path = os.path.join(dir_to_scrape, folder)
    eboot_path = os.path.join(folder_path, 'EBOOT.PBP')
    contains_eboot = 'EBOOT.PBP' in os.listdir(folder_path)
    new_folder_name = ''
    if contains_eboot:
        new_folder_name = get_game_name(eboot_path)
        new_folder_path = os.path.join(dir_to_scrape, new_folder_name)
        os.rename(folder_path, new_folder_path)
    else:
        pass
        # print(folder_path + ' does not contain EBOOT.PBP!')
