# Program to find the contents in the given directory


#importing os module
import os

path = "C:\Study\Python\Python Practice"

if os.path.exists(path) and os.path.isdir(path):
    contents = os.listdir(path)
    print(f"The contents of the directory {path} are :\n")
    for item in contents:
        print(item)
else:
    print(f"The directory {path} is incorrect or the directory does not contain any files")
