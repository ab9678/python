# camel case is nameFirst snake case is name_first
# convert camel to snake

variable = input("Enter camel case")

flag=0
condition = True
while condition is True:
    for i in range (len(variable)):
        condition = variable[i].isupper()
        if condition==True:
            store = variable[i]
            left,right = variable.split(variable[i])
            variable = left + "_" + store.lower() + right
    

print(variable)
