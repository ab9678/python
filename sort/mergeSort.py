# write a merge sort algorithm to sort elements in ascending order
def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        # recursively divide the whole array until one array has only one element
        merge_sort(left_list)
        merge_sort(right_list)
        # merge
        i = 0  # track left_list
        j = 0  # track right_list
        k = 0  # track merged list
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        # case when left array is still left but right is complete
        while i < len(left_list):
            list1[k] = left_list[i]
            i=i+1
            k=k+1
        # case when right array is still left
        while j < len(right_list):
            list1[k] = right_list[j]
            j=j+1
            k=k+1
    return list1
arr = [1, 7, 5, 6, 8, 5, 43, 65, 76, 78, 7, 6, 5, 0]
result = merge_sort(arr)
print(result)

arr.reverse()

print(arr)