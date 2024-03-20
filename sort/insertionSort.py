list1 = list ( range(10000,0,-1))
for i in range (len(list1)):
    j=i
    while j>0 and list1[j]<list1[j-1]:
        (list1[j],list1[j-1])=(list1[j-1],list1[j])
        j=j-1


print(list1)


# list1 = [8, 2, 3, 6, 5, 7]

# for i in range(1, len(list1)):
#     j = i
#     while j > 0 and list1[j] < list1[j - 1]:
#         list1[j], list1[j - 1] = list1[j - 1], list1[j]
#         j = j - 1

# print(list1)
