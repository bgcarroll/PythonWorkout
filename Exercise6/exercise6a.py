"""
Now that you’ve successfully written a translator for a single English word, let’s make
things more difficult: translate a series of English words into Pig Latin. Write a function
called pl_sentence that takes a string containing several words, separated by
spaces. (To make things easier, we won’t actually ask for a real sentence. More specifically,
there will be no capital letters or punctuation.)

    So, if someone were to call

pl_sentence('this is a test translation')

the output would be

histay isway away estay ranslationtay

Print the output on a single line, rather than with each word on a separate line.
    This exercise might seem, at least superficially, like the previous one. But here, the
emphasis is not on the Pig Latin translation. Rather, it’s on the ways we typically use
loops in Python and how loops go together with breaking strings apart and putting
them back together again. It’s also common to want to take a sequence of strings and
print them out on a single line. There are a few ways to do this, and I want you to consider
the advantages and disadvantages of each one.
"""

def pl_sentence(sentence):

    words = sentence.split()
    for i, word in enumerate(words):
        words[i] = pig_latin(word)

    print(str.join(' ', words))

def pig_latin(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string.
"""
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'

pl_sentence('this is a test translation')
