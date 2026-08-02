import random

print("🎲 Dice Roller Game")

roll = input("Roll the dice? (yes/no): ")

if roll == "yes":
    dice = random.randint(1, 6)
    print("You got:", dice)
else:
    print("Game Over!")
