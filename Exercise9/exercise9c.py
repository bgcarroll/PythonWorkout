"""
Don’t write one function that finds the largest element of a string, another that
does the same for a list, and a third that does the same for a tuple. Write just
one function that works on all of them.
"""

def largest(seq):
    return max(seq)

print(largest((7, 8, 3, 1)))
print(largest([7, 3, 1, 8]))
print(largest('7381'))
