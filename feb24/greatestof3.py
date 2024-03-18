# write a program to find the greatest of 3 numbers given by the user

num1 = int(input("Num 1: "))
num2 = int (input("Num2: "))
num3 = int(input("Num3: "))

if num1>num2 and num1>num3:
    print("Greatest number is ", num1)
elif num2>num3:
    print("Greatest number is ", num2)
else:
    print("Greatest number is ", num3, "\n")