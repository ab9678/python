list = [55,2,3,88,5,6,7,8,9]
search = int(input("Enter number to search: "))
def searchList(list1,search):
    # search = int (input("enter the number to be searched:"))
    for i in range (len(list1)):
        if(list1[i]==search):
            print("Yay!Found")
            print("The element is in the index:",i+1)
            break

searchList(list,search)