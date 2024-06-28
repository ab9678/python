# str = input ("here: ")

# # check if letter is after a number

# for i in range (len(str)-1):
#     if str[i].isnumeric():
#         if str[i+1].isalpha():
#             print("Number is in middle")
# # here: abh9b
# # Number is in middle

# # here: abhi98
plate = 'abh43'

def main():
    if checkNumMiddle(plate) is True:
        print("yes")
def checkNumMiddle(plate):
    for i in range (len(plate)-1):
        if plate[i].isnumeric():
            # for j in range(i,len(plate)-1):
            #     if plate [i+ j].isalpha():
            #         return False
            x=i
            if plate[x+1].isalpha():
                return True
        
        
main()