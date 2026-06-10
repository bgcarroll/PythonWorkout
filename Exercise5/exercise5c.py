"""
Handle punctuation—If a word ends with punctuation, that punctuation should
be shifted to the end of the translated word.
"""

def pig_latin(word):

    punctuation = ''
    if word[-1] in '!@#$%^&*':
        punctuation = word[-1]
        word = word[0:len(word) - 1]

    if word[0] in ('aeiou'):
        return word + 'way' + punctuation
    elif word[0] in ('AEIOU'):
        return str.capitalize(word + 'way') + punctuation
    elif 64 < ord(word[0]) < 91:
        return str.capitalize(word[1:]) + str.lower(word[0]) + 'ay' + punctuation
    else:
        return word[1:] + word[0] + 'ay' + punctuation

print(pig_latin("apple"))
print(pig_latin("doggy"))
print(pig_latin("python"))
print(pig_latin("computer"))
print(pig_latin("Apple"))
print(pig_latin("Doggy"))
print(pig_latin("Python"))
print(pig_latin("Computer"))
print('---')
print(pig_latin("apple!"))
print(pig_latin("doggy@"))
print(pig_latin("python#"))
print(pig_latin("computer$"))
print(pig_latin("Apple%"))
print(pig_latin("Doggy^"))
print(pig_latin("Python&"))
print(pig_latin("Computer*"))
