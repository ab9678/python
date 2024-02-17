first=0
second=1
next = 0
print(first)
print(second)
while next<=100:
    
    first=second
    second=next
    next = first + second
    if next>100:
        break
    print(next, )


    
