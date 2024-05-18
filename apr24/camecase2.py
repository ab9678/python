# def main():
#     word = input("Enter something : ")
#     i,j=0,0
#     listIndexCapital=[]
#     for i in range(len(word)):
#         if word[i].isupper():
#             j=j+1
#             listIndexCapital.append(i)
#     print(listIndexCapital)

#     print(j)

#     num=0
#     # while num != j:
#     #     word=convert_to_snake_case(word,listIndexCapital)
#     #     print(word)
#     #     num+=1
    
#     print(convert_to_snake_case(word,listIndexCapital))

# def convert_to_snake_case(word,list):
#     j=0
#     l=0
#     for k in range(0,4,1):
        
#         i = list[j]
#         left = word[l:i]
#         right = word[i+1:]
#         original = word[i].lower()
#         j=j+1
#         l+=1
#         word = left + "_" + original + right
#         print(word)
    

    
# main()
def convert_to_snake_case(word, positions):
    result = word
    for i in positions:
        left = result[:i]
        right = result[i+1:]
        original = result[i].lower()
        result = left + "_" + original + right
    return result

# Example usage:
word = "nameFirst"
positions = [4, 7]
snake_case_word = convert_to_snake_case(word, positions)
print(snake_case_word)
