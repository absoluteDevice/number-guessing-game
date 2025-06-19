import random

print("You have to pick a number between 1 and 100. You have 10 tries to guess it.")

random_number = random.randint(1, 100)
tries = 10

while tries > 0:
    try:
        number = int(input("Pick a number from 1 to 100: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if number == random_number:
        print("Congrats! You guessed the number!")
        break
    elif number > random_number:
        print("Too high!")
    else:
        print("Too low!")

    tries -= 1
    print(f"Tries left: {tries}")

if tries == 0:
    print(f"Better luck next time. The number was {random_number}.")
