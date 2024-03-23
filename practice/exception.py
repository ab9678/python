# try except usage 
# lets say we wanna take input from the user 

while (True):
    try :
        userData = int(input("Enter a number: "))
    except ValueError:
        print("Not a number , try again")   # prompt the user to try again, while true will make
    else:                                   # sure that try-except will keep excecuting until the input makes sense, in which
        break                               #case it will  execute the else , where it will break
        