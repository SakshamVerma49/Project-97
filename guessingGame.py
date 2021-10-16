import random

randomNumber = random.randint(1, 9)
chances = 0
while chances < 5:
    userGuess = int(input("Enter Your Guess: "))
    
    if userGuess == randomNumber:
        print("You Won!")
        break 
    elif userGuess < randomNumber:
        print("Incorrect, maybe try a higher number")
    else:
        print("Incorrect, probably try a lower number.")

    chances = chances+1
if chances == 5:
    print("You lose!")