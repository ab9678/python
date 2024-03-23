list = [1,4,3,5,6,7,8]

print(list[0:-1])


def binary_search(list, search,index=0):
    mid = len(list) // 2
    if len(list) <=1 and list[mid] != search:
        return -1
    if list[mid] == search:
        
        return index+mid
          
    elif search < list[mid]:
        
        return binary_search(list[0:mid],search,index)
    else :
        
        return binary_search(list[mid:],search,index+mid) 
      
list1 = [1,2,3,4,5,6,7,8,9]
list1.sort()
print(list1)