#5. Create a number guessing game using a `while` loop.
import random

seceret_num = random.randint(1, 100)

print("Welcome to the number guessing game")
print("You have to choose a number between 1 to 100")

guess = 0 

while guess != seceret_num:
    guess = int(input("Enter your number"))
    if guess < seceret_num:
        print("Too low! Try again.")
    elif guess > seceret_num:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number.")

