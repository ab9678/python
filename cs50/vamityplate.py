def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    is_valid(plate)

def is_valid(s):
    onlyAlphabetsChecker=0
    # 0 for no numbers present 1 for number is present
    # check punctuation  
    length = len(s)

    check1=s[0:2].isalpha() # first two alphabets
    check2 = s[length-1:length].isnumeric() # check if last is numeric
    check3 = True # no punctuations
    for i in range(0 , length):
        if s[i].isalnum() is False: # check for punctuations
            check3 = False
    # print(check1,check2)
    if 2<=length<=6:

        if check1 is True and check3 is True and check2 is False:
            for i in range (0,len(s)):
                if s[i].isnumeric() is True:
                    onlyAlphabetsChecker = 1
                else:
                    return True
        if check1 is True and check2 is True and check3 is True:
            finalCheck=breakString(s,length)
        else:
            return False
        # print(finalCheck,": finalcheck")
        if finalCheck == False:
            # print("wrong")
            return False
        return True
    else:
        print("Length too small or too big")

def breakString(s,length):
    i=-1
    for i in range (0,length):
        if s[i].isnumeric():
            index = i
            break
    # print(index)
    str1 = s[0:index]
    str2 = s[index:length]
    # print(str1,"\n",str2)
    if i == -1:
        return False
    if check2Halves(str1,str2):
        return True
    else:
        return False

def check2Halves(str1,str2):
    if str2[0] == '0':
        return False
    for i in range (len(str2)):
        if str2[i].isalpha():
            # print("Alphabet comes in the middle")
            return False
    return True

main()