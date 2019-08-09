# ================================================================================
# Created by: Alex L.
# Date:       8/25/2018
# Info:       This Python script sorts files by extension in 'source' directory and
#             copies files into 'destination' in appropriate subdirectories
# ================================================================================

import os           # This module provides functions for interacting with the OS
import shutil       # This module provides functions for copying files and directories
import time         # This module provides various functions to manipulate time values

source = 'E:\RAZNOE'           # Source directory
destination = 'E:\SORTED'      # Destination directory

total_files_moved = 0    # Total files moved


# This function sorts files by extension
def sort (source, destination):
    global total_files_moved
    for root, dirs, files in os.walk(source):          # Method os.walk allows checking subdirectories
        for file in files:
            extension = (os.path.splitext(file)[1][1:])
            destinationPath = os.path.join(destination, extension)

            if os.path.exists(destinationPath) != True:
                os.mkdir(destinationPath)
            if os.path.exists(os.path.join(destinationPath, file)):
                print('This file was not copied - it exists: ' + os.path.join(root, file))
            else:
                shutil.copy2(os.path.join(root, file), destinationPath)
                total_files_moved += 1                  # Count number of files moved


starttime = time.asctime()          # Gets Start Time

sort(source, destination)

finishtime = time.asctime()         # Gets Finish Time

print('############################################################')
print('Start Time: ' + str(starttime))
print('Total files moved: ' + str(total_files_moved))
print('Finish Time: ' + str(finishtime))
print('############################################################')