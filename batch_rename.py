"""
batch move 
created by Soffi Zahir
"""
import os
import re
import shutil
from shutil import copy
from datetime import date

# count number of file removed
total_files_copied = 0
total_errors = 0
PATTERN = ""
EXCLUDE = ""


def set_des_dir(source_dir, pattern):
    # directory where to store few files
    assaki = str(date.today())
    des_dir = os.path.join(os.path.dirname(source_dir), PATTERN.upper() + assaki)
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)
    return des_dir


def moveto(src):
    try:
        shutil.move(src, DES_DIR, copy_function=copy)
        print("moving ...", src)
        global total_files_copied
        total_files_copied += 1

    except shutil.Error:
        print(f"can't copy file {src} probably file already exist")
        global total_errors
        total_errors += 1


def dirTree(dir_name):
    dirs = os.listdir(dir_name)
    for name in dirs:
        abs_path = os.path.join(dir_name, name)
        if not os.path.isdir(abs_path):
            if re.search(PATTERN.lower(), name.lower()) and \
                    not re.search(os.path.splitext(name)[1], EXCLUDE):
                # print(name)
                moveto(abs_path)
        else:
            dirTree(abs_path)


# dirTree(SOURCE_DIR)
print("""
	¤this is a bêta version¤
Hello & welcome to easy move programme
-first thing you have to give a pattern 
-then a sibling directory where to search
-the programme will traverse directories recursively so all files will be scanned
-the programme store files in your home directory with a name "pattern[date]"
""")

# where to search files
SOURCE_DIR = input("name of directory (absolute path ) >>> \n")

# pattern to search
PATTERN = input("pattern >>> \n")

# pattern to exclude
EXCLUDE = input("exclude >>> \n")


# destination directory
DES_DIR = set_des_dir(SOURCE_DIR, PATTERN)

dirTree(SOURCE_DIR)
print("Total file copied : ", total_files_copied)
print("Total copy failed : ", total_errors)
