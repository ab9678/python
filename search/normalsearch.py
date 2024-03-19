list1 = [1,2,3,4,5,6,7,8,9]
search = int (input("enter the number to be searched:"))
for i in range (len(list1)):
    if(list1[i]==search):
        print("Yay!")
        break