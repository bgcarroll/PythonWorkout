"""
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), the Pig Latin translation should be similarly
capitalized.
"""

def pig_latin(word):

    if word[0] in ('aeiou'):
        return word + 'way'
    elif word[0] in ('AEIOU'):
        return str.capitalize(word + 'way')
    elif 64 < ord(word[0]) < 91:
        return str.capitalize(word[1:]) + str.lower(word[0]) + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_latin("apple"))
print(pig_latin("doggy"))
print(pig_latin("python"))
print(pig_latin("computer"))
print(pig_latin("Apple"))
print(pig_latin("Doggy"))
print(pig_latin("Python"))
print(pig_latin("Computer"))
