# write a code in python to implement merge for a\b i.e return those elements which are in
# A ,but not in B

def merge(list1):
    if len(list1) > 1:
        midPt = len(list1) // 2

        left_half = list1[:midPt]
        right_half = list1[midPt:]

        merge(left_half)
        merge(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j] and left_half[i] != right_half[j]:
                list1[k] = left_half[i]
                i += 1
            elif left_half[i] > right_half[j] and left_half[i] != right_half[j]:
                list1[k] = right_half[j]
                j += 1
        k += 1

        while i < len(left_half):
            list1[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list1[k] = right_half[j]
            j += 1
            k += 1
        return list1


listA = [1, 5, 4, 3, 1, 7, 8, 5, 4, 3]

result=merge(listA)
print(result)