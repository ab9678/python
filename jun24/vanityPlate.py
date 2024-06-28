
import subprocess
import os

'''
a python code to self-destruct the file
'''

# find a way to pwd and return the directory to a variable, that way
# the file path won't have to be hard-coded

subprocess.run(["pwd"], shell=True)


#file_path = "/home/abhigyan/Documents/GITHUB_FILES/python/jun24/new.txt"
#filePath = filepath + "/abc.txt"
#print(filePath)
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
        os.remove(filePath)
    else:
        print("sucessfully authorised")

main()

def new():
    ...


















