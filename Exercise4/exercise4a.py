"""
    For this exercise, you need to write a function (hex_output) that asks the user for a
hex number and prints the decimal equivalent. That is, if the user enters 50, you’ll
assume that it’s a hex number (equal to 0x50) and will print the value 80 to the screen.
And no, you shouldn’t convert the number all at once using the int function,
although it’s permissible to use int one digit at a time.
    This exercise isn’t meant to test your math skills; you can get the hex equivalent of
integers with the hex function, but most people don’t need that in their day-to-day
lives. However, this does touch on the conversion (in various ways) across types that we
can do in Python, thanks to the fact that sequences (e.g., strings) are iterable. Also
consider the built-in functions that you can use to solve this problem even more easily
than if you had to write things from scratch.
"""

def hex_output():

    hex_string = input("Enter a hex number: ")
    hex_reversed = hex_string[::-1]

    base_ten = 0
    power = 0
    for char in hex_reversed:
        if char == '-':
            base_ten *= -1
            break
        base_ten += int(char, 16) * (16 ** power)
        power += 1

    print(f'base 10 = {base_ten}')

hex_output()
