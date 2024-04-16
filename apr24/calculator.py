
def calculator(n1,n2,op):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "/":
        return n1/n2
    elif op == "*":
        return n1*n2
    else:
        return "INVALID"







def main():

    num1= int(input("Enter a number"))
    num2= int(input("Enter the second number"))

    operator = input("Enter operator")

    res = calculator(num1,num2,operator)
    print(res)


main()