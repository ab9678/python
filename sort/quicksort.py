# Quick sort is that we take one element and mark it as base , now move all elements smaller to the left and larger ones to the right. Now sort the halves , and finally we get a sorted array

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        lower=[]
        upper=[]

        for i in range (len(arr)):
            if arr[i] < pivot:
                lower.append(arr[i])
            else:
                upper.append(arr[i])
    
    return quick_sort(lower) + [pivot] + quick_sort(upper)


print(quick_sort([3,6,5,7,8,9,2,1,0]))
          
