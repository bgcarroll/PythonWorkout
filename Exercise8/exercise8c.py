"""
Which is the last word, alphabetically, in a text file?
"""

def last_word(filepath):

    with open(filepath) as file:
        lines = file.readlines()

    words = sorted([
        word
        for line in lines
        for word in str.split(line)
    ])

    print(words[len(words) -1])

last_word("./fileA.txt")
