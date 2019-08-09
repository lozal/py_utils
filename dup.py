# ================================================================================
# Created by: Alex L.
# Date:       7/18/2018
# Info:       This Python script removes duplicate files in 'path' directory
#             and in subdirectories
# ================================================================================

import os           # This module provides functions for interacting with the OS
import hashlib      # This module provides allows to get MD5 Checksum
import time         # This module provides various functions to manipulate time values

path = 'E:\RAZNOE'  # Target directory

dup_counter = 0     # Total duplicates deleted


# Function for MD5 Checksum calculating for a file.
# The function takes one file as an argument and returns MD5 Checksum for that file
def md5checksum(file):
    return hashlib.md5(open(file, 'rb').read()).hexdigest()
    # hexdigest()is returned as a string of length 32, containing only hexadecimal digits.
    # This used in non-binary environments


# This function removes duplicate files
def rm_duplicate(path):
    global dup_counter
    if not os.path.isdir(path):  # It makes sure that the given directory exists
        print('The given directory does not exist! Please input correct directory.')
    else:
        md5_dict = {}                            # Dictionary for function operating
        for root, dirs, files in os.walk(path):  # Method os.walk allows checking subdirectories
            for file in files:
                if not md5checksum(os.path.join(root, file)) in md5_dict:
                    print('Checking for duplicate in', root, 'directory for file:', file)
                    md5_dict.update({md5checksum(os.path.join(root, file)): [os.path.join(root, file)]})
                else:
                    print('Found a duplicate in', root, 'directory for file:', file)
                    md5_dict[md5checksum(os.path.join(root, file))].append(os.path.join(root, file))
        for key in md5_dict:
            while len(md5_dict[key]) > 1:
                for dup_item in md5_dict[key]:
                    print('Removing duplicate:', dup_item)
                    dup_counter += 1              # Counting duplicates removed
                    os.remove(dup_item)
                    md5_dict[key].remove(dup_item)
        if dup_counter > 0:
            print('Removed', dup_counter, 'duplicates')
        else:
            print('Found no duplicates in this directory')
        print('Checking for duplicate is complete!')


starttime = time.asctime()          # Gets Start Time

rm_duplicate(path)

finishtime = time.asctime()         # Gets Finish Time

print('############################################################')
print('Start Time: ' + str(starttime))
print('Total duplicates removed: ', dup_counter)
print('Finish Time: ' + str(finishtime))
print('############################################################')