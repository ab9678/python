# Create a python program to make a binary search through a list
# This is wrong coz here index is not calculating for the missed out "mid" elements index
def binary_search(list, search,index=0):
    
    

    mid = len(list) // 2

    if list[mid] == search:
        return list[mid]
    
    elif search < list[mid]:
        return binary_search(list[0:mid],search)
    else :
        index = index + mid
        return binary_search(list[mid:],search)
        
    
    
        
    
list1 = [1, 3, 2, 4, 5, 6]

list1.sort()
print(list1)
search = int(input("Enter the number to be searched: "))
result = binary_search(list1, search)
print(result)

