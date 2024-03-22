"""
write a pyton program to search for a number in a list , replace that number with
something the user wants and return a sorted list using mergesort

"""


def mergesort(listM):
    if len(listM) > 1:

        mid = len(listM) // 2

        left_half = listM[:mid]
        right_half = listM[mid:]

        # sort both halves(divide until one element is left)

        mergesort(left_half)
        mergesort(right_half)

        i = 0  # keep track of the indices f left
        j = 0  # track indices of right
        k = 0  # track indices of merged list

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                listM[k] = left_half[i]

                i += 1
                k += 1
            else:  # when right half is less or smaller
                listM[k] = right_half[j]
                j += 1
                k += 1

        # now left half is larger than the right half
        # While i is still less than length of left_half
        while i < len(left_half):
            listM[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            listM[k] = right_half[j]
            j += 1
            k += 1

        return listM


originalList = []
length = int(input("Enter the range: "))
for i in range(length):
    a = int(input("Enter elements here: "))
    originalList.append(a)

sortedList = mergesort(originalList)
print(sortedList)

search = int(input("Enter the number to be searched: "))


def binarysearch(sortedList, search, index=0):
    mid = len(sortedList) // 2

    if len(sortedList) <= 1 and sortedList[mid] != search:
        return -1

    if sortedList[mid] == search:
        return mid + index
    elif search > sortedList[mid]:
        return binarysearch(sortedList[mid:], search, index + mid)
    else:
        return binarysearch(sortedList[:mid], search, index)


R_index = binarysearch(sortedList, search)
# print(R_index)
if R_index != -1:
    print("We found", sortedList[R_index], "at", R_index)

    operand = input("Do you want to edit the element?(y/n):")
    if operand == "y":
        replace = int(input("Enter new element: "))
        sortedList[R_index] = replace
        print(sortedList)
    else:
        print("Thank you")

else:
    print("Your element is not found")

sortedList = mergesort(sortedList)
print("Your Final sorted list is", sortedList)
