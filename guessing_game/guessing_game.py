# Guess the number game
import random

print('Hello. What is your name?')
name = input()

print(f"Well, {name} I am thinking of a number between 1 and 20")
secret_number = random.randint(1, 20)

for guess_taken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is for correct guess
    print(f'You have {6 - guess_taken} guesses left.')

if guess == secret_number:
    print(f'Good job, {name}! You guessed my number in {guess_taken} guesses.')
else:
    print(f'Nope. The number I was thinking of was {secret_number}')


