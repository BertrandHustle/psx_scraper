#! python
from struct import unpack_from
import argparse
import os

"""
    Copyright (C) 2020  Scott Greenberg

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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


def get_game_name(filename: str):
    """
    retrieves game name from pbp file
    :param filename: path to pbp file
    :return: game name or False
    """
    gamename = b''
    with open(filename, 'rb') as eboot:
        eboot.seek(0x24)
        pbp_verification_offset = eboot.read(4)
        eboot.seek(int.from_bytes(pbp_verification_offset, "little"))
        pbp_verification_string = eboot.read(8)
        # check the bytes for information that confirms the pbpfile is from a psx game
        # PSISOIMG is for single disc games and PSTITLEI is for multi-disc games
        # based on evertonstz's contributions
        if pbp_verification_string == b'PSISOIMG' or pbp_verification_string == b'PSTITLEI':
            eboot.seek(0x358)
            while True:
                current_byte = eboot.read(1)
                if current_byte == b'\x00':
                    break
                else:
                    try:
                        gamename += current_byte
                    except UnicodeDecodeError:
                        break
        else:
            return False
    gamename = gamename.decode()
    if len(gamename) > 31:
        return gamename.replace(' ', '')[:21].replace('\x00', '').replace(':', '')
    else:
        return gamename.replace('\x00', '')


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
