import shutil
import os

source = './Folder_A/'

destination = './Folder_B/'

files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
