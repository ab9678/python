# append to list only when a unique item is captured. sort alphabatically

groceryDict = {}

while (True):

    try:
        grocery = input()
        
        if grocery not in groceryDict:
            groceryDict[grocery]=1
        elif grocery in groceryDict:
            
            groceryDict[grocery]+=1

    except EOFError:

        sortedkeys=sorted(groceryDict.keys())
        
        for i in sortedkeys:
            print(f"{groceryDict[i]}.{i.upper()}")
                    # here we are printing the value of i in the dict, here after sorting the i's are stored in a list, so t access the i's dictionary content we can access grocerydict of i where the 'i' key has a certain value which is the count, refer above code , printing the value associated with the key->i.
        break

l = [1,2]
sorted(l)

print(l)