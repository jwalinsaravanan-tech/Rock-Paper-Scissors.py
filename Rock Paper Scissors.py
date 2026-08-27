import random

choices = ("rock", "paper", "scissors")

player = input("Choose rock, paper or scissors: ")

computer = random.choice(choices)

print("you chose:", player)
print("computer chose:", computer)

if player == computer:
    print("Draw")
    

elif player == "rock" and computer == "scissors":
        print("You lose!")


elif player == "rock" and computer == "paper":
        print("You win!")


elif player == "paper" and computer == "rock":
        print("You lose!")


elif player == "paper" and computer == "scissors":
        print("You Win!")


elif player == "scissors" and computer == "paper":
        print("You win!")


elif player == "scissors" and computer == "rock":
        print("You lose!")
