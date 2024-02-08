import random


def random_number():
    return random.randint(1,101)


def set_difficulty(difficult):
    if difficult == "easy":
        return 10
    else:
        return 5


# -------------------
print("Welcome to the Number Guessing Game!")
difficulty = input("Please select a difficulty![ easy (10hp) / hard (5hp) ]\n :")
health = set_difficulty(difficulty)
print("I'm thinking of a number between 1 and 100.")
number = random_number()


print("You have " + str(health) + " health")
while health > 0:
    guess = int(input(f"Guess a number between 1 and 100: "))

    if guess > number:
        print("High! decrease the altitude!")
        health -= 1

    elif guess < number:
        print("Low! increase the altitude!")
        health -= 1

    else:
        break

if guess == number:
    print(f"Congratulations! You guessed the correct number! You have {health} health left.")
else:
    print("Sorry, you have no health left. You lose!")
