# def frequency(l):
#     frequentElement=[]
#     l.sort()
#     print(l)
#     i=0
#     max_freq =1
#     freq = 1
#     while i+1 <= (len(l)-1):
        
#         if l[i]==l[i+1]:
#             freq+=1
#             # print(freq)
        

#         else:
#             if freq>max_freq:

#                 max_freq = freq

#                 print(l[i],freq)

                
#                 frequentElement=[l[i]]

#             elif freq == max_freq:
#                 frequentElement.append(l[i])
#         i+=1
#         freq=1
#     # print(max_freq)
#     # i=0
#     # freq=1
#     # while i+1 <= (len(l)-1):
        
#     #     if l[i] == l[i+1]:
#     #         freq +=1
#     #         # print(freq)
        
#     #     if freq == max_freq and l[i] not in frequentElement:
#     #         frequentElement.append(l[i])
#     #         freq = 1
#     #     i+=1
#     return frequentElement




        

            


    

# print(frequency([13,12,11,11,13,14,13,7,11,13,14,12,14]))
# # [7, 11, 11, 12, 12, 13, 13, 13, 13, 14, 14]


def frequency(l):
    l.sort()
    print(l)
    max_freq = 1
    freq = 1
    frequent_elements = []

    # Traverse the sorted list and count frequencies
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            freq += 1
        else:
            if freq > max_freq:
                max_freq = freq
                frequent_elements = [l[i - 1]]  # Start a new list with the current element
            elif freq == max_freq:
                frequent_elements.append(l[i - 1])  # Append the element to the list

            freq = 1  # Reset frequency counter for the next element

    # Final check for the last element in the list
    if freq > max_freq:
        frequent_elements = [l[-1]]
    elif freq == max_freq:
        frequent_elements.append(l[-1])

    return frequent_elements

# Example usage
print(frequency([13, 12,11, 11,11, 13, 14, 13, 7, 11, 13, 14,14, 12,14]))
