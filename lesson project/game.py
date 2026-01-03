Greetings = "hello "
name = input(' name?')
print(Greetings + name)


import random

print("🎮 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 20.")


secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} tries.",name)
        break