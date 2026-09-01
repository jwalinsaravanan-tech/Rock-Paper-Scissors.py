Heads = 0
Tails = 0

import random

Amount = int(input("How many time do you want to toss the coin??"))

for i in range(Amount):
    coin = random.choice(("Heads", "Tails"))

    if coin == "Heads":
        Heads = Heads + 1

    if coin == "Tails":
        Tails = Tails + 1

print("Tails:", Tails)
print("Heads:", Heads)
