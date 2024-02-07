number = 10
max_guesses = 3
guess_count = 0

print("I'm thinking of a number...")

while guess_count < max_guesses:
    guess = input("What number am I thinking of? ")
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    guess = int(guess)
    guess_count += 1
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! That's too low. Try again.")
    else:
        print("Sorry! That's too high. Try again.")
else:
    print(f"Sorry! You've reached the maximum number of guesses. The number was {number}.")

