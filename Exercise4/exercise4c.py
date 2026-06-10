"""
Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line.
"""

def triangle():

    name = input("Enter your name: ")

    for length in range(len(name)):
        print(name[:length+1])

triangle()
