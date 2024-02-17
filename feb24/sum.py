# input 2 numbers and print their sum

num1 = int (input("Enter a Number: "))
num2 = int(input("Enter another number: "))
flag=0
while True:#in python while true run the code at least once coz the condition is break statement , which is at the end_
    operation = input("Specify Opeartor:  + , - , / , * , **")

    if(operation == "+"):
        print(num1+num2)
        flag =0
    elif(operation == "-"):
        print(num1-num2)
        flag =0
    elif(operation == "/"):
        print(num1/num2)
        flag =0
    elif(operation == "*"):
        print(num1*num2)
        flag =0
    elif(operation=="**"):
        print(num1**num2)
        flag =0
    else:
        print("Invalid operator")
        flag=1
    if(flag == 0):
        break




