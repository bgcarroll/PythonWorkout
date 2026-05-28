import random


def guessing_game():

    num_tries = 5

    # random.seed(0)  # enable for testing
    random_number = random.randint(1, 100)

    guess_count = 0

    while guess_count < num_tries:
        guess = int(input("Guess a number between 1 and 100: "))
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
