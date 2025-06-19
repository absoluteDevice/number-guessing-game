import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. You have 10 tries to guess it.")

random_number = random.randint(1, 100)
tries = 10

while tries > 0:
    try:
        number = int(input("Pick a number from 1 to 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if number == random_number:
        print("Congrats! You guessed the number!")
        break
    elif number > random_number:
        print("Too high!")
    else:
        print("Too low!")

    tries -= 1
    print(f"Tries left: {tries}\n")

if tries == 0:
    print(f"You lose. The number was {random_number}.")
