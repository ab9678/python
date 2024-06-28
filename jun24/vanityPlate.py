'''
a python code to self destruct the file
'''
file_path = "/home/abhigyan/Documents/GITHUB_FILES/python/jun24/new.txt"

import subprocess
import os
import shutil

def main():
    flag = 2
    name = input("who are you? ").lower()

    if name == "abhigyan":
        flag = 1
    else:
        flag = 0

    checkauth(flag)

   

def checkauth(flag):

    if flag == 0:
        os.remove(file_path)
    else:
        print("sucessfully authorised")


main()






















