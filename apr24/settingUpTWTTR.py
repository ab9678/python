# write a program where when the user writes a full line we just return the word but 
# the vowels are ommitted

string = input("Enter anything: ").lower()
vowels = ['a','e','i','o','u']
realword = ""

for i in range(len(string)):
    if string[i] not in vowels:
        realword+=string[i]

print(realword)