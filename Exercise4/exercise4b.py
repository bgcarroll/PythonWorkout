"""
Reimplement the solution for this exercise such that it doesn’t use the int function
at all, but rather uses the built-in ord and chr functions to identify the character.
This implementation should be more robust, ignoring characters that
aren’t legal for the entered number base.
"""

def hex_output():

    hex_string = input("Enter a hex number: ")
    is_negative = hex_string[0] == '-'
    hex_reversed = hex_string[::-1]

    base_ten = 0
    power = 0
    for char in hex_reversed:
        ord_char = ord(char)
        print(f'ord(char) = {ord_char}')
        if (64 < ord_char < 71) or (47 < ord_char < 58):
            ord_char_val = int(char, 16)
        else:
            # ran into an invalid char, skip it
            continue

        base_ten += ord_char_val * (16 ** power)
        power += 1

    if is_negative:
        base_ten *= -1

    print(f'base 10 = {base_ten}')

hex_output()
