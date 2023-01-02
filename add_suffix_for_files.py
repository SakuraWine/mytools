import os
import glob
import argparse


# initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="target directory path")
parser.add_argument("-s", "--suffix", help="suffix")
args = parser.parse_args()
target_directory_path = args.path
suffix = args.suffix
# check input
if target_directory_path[-1] != "/":
    target_directory_path = target_directory_path + "/"
if not os.path.exists(target_directory_path):
    print("target directory not found.")
    exit(-1)
# execute
files = glob.glob(target_directory_path + "*")
for file in files:
    splitted_filename = os.path.splitext(file.replace(target_directory_path, ""))
    filename = splitted_filename[0] + suffix + splitted_filename[1]
    print(filename)
    os.rename(file, target_directory_path + filename)
