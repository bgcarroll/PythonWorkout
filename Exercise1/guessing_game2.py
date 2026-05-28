import random


def guessing_game():

    num_tries = 5

    bases = {2,8,10,16}
    rand_base = random.choice(list(bases))
    random_number = random.randint(1, 100)

    guess_count = 0

    while guess_count < num_tries:
        raw_guess = input(f'Guess a number between 1 and 100, Enter in base {rand_base}: ')
        try:
            guess = int(raw_guess, rand_base)
        except ValueError:
            raw_guess = input(f'Enter in base {rand_base}!!: ')
            guess = int(raw_guess, rand_base)
        guess_count += 1

        if guess > random_number and guess_count < num_tries:
            print("Too high!, try again")

        if guess > random_number and guess_count == num_tries:
            print("Too high!, Game Over!")

        if guess < random_number and guess_count < num_tries:
            print("Too low!, try again")

        if guess < random_number and guess_count == num_tries:
            print("Too low!, Game Over!")

        if guess == random_number:
            print("You guessed correctly! Game Over!")
            break


guessing_game()
