#built-in
import os
import argparse
#project
import part_number_finder

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--target_dir', help='directory containing psx iso folders (i.e. from PSX2PSP)')
args = parser.parse_args()

target_dir = args.target_dir
psx_dirs = os.listdir(target_dir)

# col2 = serial num
# col3 = game name

pnf = part_number_finder.PartNumberFinder()

pnf.get_game_name_from_part_number('test')