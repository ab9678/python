import math
from sys import set_int_max_str_digits
print("enter Number \t")
a=int(input())

set_int_max_str_digits(100000)
def factorial(num):
    if(num==1):
        return 1
    elif(num == 0):
        return 0
    else:
        return num * factorial(num-1)
    
result=factorial(a)
print(result)

# for pyhton the limit is 999
