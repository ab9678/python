# Sort a list in ascending order using selction sort algorithm

# take elemnt 0 , set it as samllest , scan throught the list , swap 0 with smallest , repeat but now start from 1

def selection_sort(list):

    for i in range (0,len(list)):
        smallest=i  # store the index of the smallest let-be value
        for j in range (i+1,len(list)): # Also we want to search from 2nd element sice 1st is already set as base/smallest , hence i+1# if nothing is mentioned step is automatically set as 1
            if list[j]<list[smallest]:
                smallest=j  # update the index of the smallest variable with the real smallest value's index

        list[i],list[smallest]=list[smallest],list[i]   
    
    return list

original = [1,0.05,4,3,21,7,415,2,9]
result=selection_sort(original)
print(result)


