# ================================================================================
# Created by: Alex L.
# Date:       8/8/2019
# Info:       This Python script removes files older than X days and empty directories in target directories
# ================================================================================
import os           # This module provides functions for interacting with the OS
import time         # This module provides various functions to manipulate time values

age = 3     # Max age of file to stay (in days), older will be deleted

# Target directories
directories = [
            'E:\RAZNOE1',
            'E:\RAZNOE2',
          ]
total_files_removed = 0   # Total files removed
total_dirs_removed = 0    # Total empty folders removed
total_size_removed = 0    # Total size of all files removed (in bytes)

nowTime = time.time()              # Gets Current time in seconds
targetTime = nowTime - 60*60*24*age  # Target time: Current time minus age (days) (in seconds)


# This function removes files older than X days
def remove_old_files(directory):
    global total_files_removed
    global total_size_removed
    for path, dirs, files in os.walk(directory):
        for file in files:
            fileName = os.path.join(path, file)          # Gets full path to file
            fileTime = os.path.getmtime(fileName)        # Gets file time
            if fileTime < targetTime:
                sizeFile = os.path.getsize(fileName)     # Gets file size
                total_files_removed += 1                 # Counts number of files removed
                total_size_removed += sizeFile           # Counts total size of all files removed
                print('Removing old file: ' + str(fileName))
                os.remove(fileName)                      # Removing old file


# This function removes empty directories
def remove_empty_dir(directory):
    global total_dirs_removed
    empty_folders = 0
    for path, dirs, files in os.walk(directory):
        if (not dirs) and (not files):
            total_dirs_removed += 1
            empty_folders += 1
            print('Removing empty directory: ' + str(path))
            os.rmdir(path)                                # Removing empty directory
    if empty_folders > 0:
        remove_empty_dir(directory)


starttime = time.asctime()          # Gets Start Time

for directory in directories:
    remove_old_files(directory)     # Removing old files
    remove_empty_dir(directory)     # Removing empty folders

finishtime = time.asctime()         # Gets Finish Time

print('############################################################')
print('Start Time: ' + str(starttime))
print('Total files removed: ' + str(total_files_removed))
print('Total size of all files removed: ' + str(round((float(total_size_removed/1024/1024)), 3)) + ' MB')
print('Total empty folders removed: ' + str(total_dirs_removed))
print('Finish Time: ' + str(finishtime))
print('############################################################')
