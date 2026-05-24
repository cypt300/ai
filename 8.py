# guess the number

import random

num = random.randint(1, 100)
attempts = 5

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

while attempts:
    guess = int(input("Guess the number (1 - 100): "))

    if guess == num:
        print(f"Congratulations! You guessed the number {num} correctly!")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1

if attempts == 0 and guess != num:
    print(f"Sorry, you've run out of attempts! The correct number was {num}.")
