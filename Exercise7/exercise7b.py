"""
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), the Ubbi Dubbi translation should be similarly
capitalized.
"""

def ubbi_dubbi(word):

    my_new_word = ''

    for letter in word:
        if letter in 'aeiou':
            my_new_word += 'ub' + letter
        elif letter in 'AEIOU':
            my_new_word += 'Ub' + letter.lower()
        else:
            my_new_word += letter

    return my_new_word

print(ubbi_dubbi("cat"))
print(ubbi_dubbi("soap"))
print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("elephant"))
print(ubbi_dubbi("Cat"))
print(ubbi_dubbi("Soap"))
print(ubbi_dubbi("Octopus"))
print(ubbi_dubbi("Elephant"))
