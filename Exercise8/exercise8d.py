"""
Which is the longest word in a text file?
"""

def longest_word(filepath):

    with open(filepath) as file:
        lines = file.readlines()

    longest_word = ''
    for line in lines:
        for word in str.split(line):
            if len(word) >  len(longest_word):
                longest_word = word

    print(longest_word)

longest_word("./fileA.txt")
