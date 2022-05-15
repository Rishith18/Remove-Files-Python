import os
import time
import shutil

days = 0
path = input("Enter path to check: ")

name, ext = os.path.splitext(path)

print(name, " and " , ext)

walk1 = os.walk(path)

print(walk1)

"""if os.path.exists(path):
    print("valid path")
    if ext == "":
        shutil.rmtree(path)
        print("folder deleted")
    else:
        os.remove(path)
        print("file deleted")
else:
    print("invalid path")"""