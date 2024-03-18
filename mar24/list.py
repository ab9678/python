list1 = [1,2,3,4,5]

list2 = list1

list1[2]=9


print(list1)
print(list2)

list3 = list(input("enter list \t"))

for i in range (9,18,3):
    list1.append(i)

print(list1)
print(list3)