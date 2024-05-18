'''
code to find out duplicates in a already sorted array

'''
array = [1,1,2,3,3,5]
for arrow1 in range(0,5):    
    if array[arrow1]==array[arrow1+1]:
        print(array[arrow1])
