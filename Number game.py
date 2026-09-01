guesses = 0

import random

number = random.randrange(1,100)

print("Welcome to the number guessing game!You get five guesses, GOOD LUCK.")

player = int(input("What do you think the number is?"))

while player!=number:
    guesses = guesses + 1
    print("Wrong answer, try again!")
    if player > number:
        print("Too high")
    else:
        print("Too low")
    player = int(input("What do you think the number is?"))
    if guesses == 4:
        print("you have used all five guesses!")
        break

if player == number:
    print("Congratulations! You win")

print("The Correct number was:", number)
