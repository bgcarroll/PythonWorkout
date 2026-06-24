"""
Don’t write one function to find the largest word in a file that works on files and
another that works on the io.StringIO (http://mng.bz/PAOP) file simulator
used in testing. Write one function that works on both.
"""

from io import StringIO

def largest_word(file):

    largest = ''
    for line in file:
        for word in str.split(line):
            if len(word) > len(largest):
                largest = word

    return largest

data = "While these tasks might seem simple, they crop up on a regular basis in production Python code. Zebra. Supercalifragilisticexpialidocious. The fact that these data structures and methods are written in C and have been around for many years means they’re also highly efficient—and not worth reinventing"
virtual_file = StringIO(data)
virtual_file.seek(0)
print(largest_word(virtual_file))
virtual_file.close()

with open("./fileA.txt") as file:
    print(largest_word(file))
