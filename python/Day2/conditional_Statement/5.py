import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong Guess!")
    print("The correct number was:", secret_number)