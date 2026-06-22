import random

secret_number = random.randint(1, 100)
user_guess = None
guess_count = 0
guess_limit = 5
out_of_guesses = False

print("\nWelcome to a RUSSIAN ROULETTE")
print(f"You are to think of a number within 1 and 100 and you have {guess_limit} chances")

while secret_number != user_guess and not out_of_guesses:
    if guess_count < guess_limit:
        try:
            user_guess = int(input(f"\n Guess {guess_count + 1} / {guess_limit} Enter a number: "))
            guess_count += 1

            if user_guess < secret_number:
                print("Too low, aim at a higher number.")
            else:
                print("Too high, aim at a lower number.")
        except ValueError:
            print("Invalid input, please enter a valid integer.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print(f"Ooooopss! Sorry you lose, the correct number is  {secret_number}")
else:
    print(f"Huurrraaayyy! Congratulations you won after {guess_count} attempt")