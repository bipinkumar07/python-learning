# Number Guessing Game

secret_number = 7

guess = int(input("Guess a number (1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print("Wrong guess. Try again!")
    print("The correct number was", secret_number)
