"""
Don’t write one function that squares integers and another that squares floats.
Write one function that handles all numbers.
"""

def squares(num):
    return num ** 2

print(squares(5))
print(squares(5.0))
