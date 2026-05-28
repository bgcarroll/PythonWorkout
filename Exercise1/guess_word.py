import random

from english_words import get_english_words_set


def guess_word():

    num_tries = 5

    # Fetch the word list
    all_words = get_english_words_set(['web2'], lower=True)

    # Filter for words of length 3
    three_letter_words = {word for word in all_words if len(word) == 3}

    random_word = random.choice(list(three_letter_words))
    print(random_word) # for testing

    guess_count = 0

    while guess_count < num_tries:
        guess = input("Guess a word with 3 letters: ")
        guess_count += 1

        if guess == random_word:
            print("Correct! Game Over!")
            break

        if guess != random_word and guess_count < num_tries:
            print("Wrong! Try again")

        if guess != random_word and guess_count == num_tries:
            print("Wrong! Game Over!")

guess_word()
