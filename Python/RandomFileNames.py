import os
import tkinter
from tkinter.filedialog import askdirectory
import string
import random

def randomName(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def rename(filename, folder):
    root, ext = os.path.splitext(filename)
    os.rename(folder + "\\" + filename, folder + "\\" + randomName() + ext) #Can't get os.path.join to work, since it mixes backslashes and forward slashes in a weird way
                                                                            #Thus, I am resorting to binding it to windows filesystem backslashes

try:
    folder = askdirectory()
    dirpath, dirnames, filenames = os.walk(folder)
    for file in filenames:
        
        rename(file, folder)
except FileNotFoundError as fnfe:
    print("File Ain't Found!! " + repr(fnfe))
except Exception as ex:
    print(repr(ex))
