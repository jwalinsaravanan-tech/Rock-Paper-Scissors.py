import random

choices = ("Head", "Tails")

player = input("Heads or Tails:")

Computer = random.choice(choices)

print("You chose:", player)
print("The coin landed on:", Computer)

if player == Computer:
    print("You were right and you win the money!")

elif player == "Heads" and Computer == "Tails":
    print("You were wrong, good luck next time!")

elif player == "Tails" and Computer == "Heads":
    print("You were wrong, good luck next time!")
