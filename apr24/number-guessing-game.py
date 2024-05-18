'''
Create a number guessing game where the computer generates a random 
number between 1 and 100, and the user has to guess it. Provide hints such as
"Too high" or "Too low" after each guess. The game should continue until the 
user correctly guesses the number.

'''
import random
flag = True
number = random.randint(1,100)
while flag is True:
    
    guess = int(input("Guess: "))
    if number<guess:
        print("Too high")
    elif number>guess:
        print("Too low")
    else:
        print("Gotcha!")
        flag = False
