import random

print("Welcome to Dice Roller!")
while True:
    roll = input("Press Enter to roll the dice or type 'exit' to quit: ")
    if roll.lower() == 'exit':
        print("Thanks for playing!")
        break
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}")