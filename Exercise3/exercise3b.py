'''
Write a function that takes a float and two integers (before and after). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678, 2, and
3, the return value should be 34.567.
'''

import math

def before_after(number, before, after):

    negative = number < 0
    number = abs(number)

    before_num = int(number) % (10 ** before)

    after_num = number - int(number)
    after_num = math.trunc(after_num * (10 ** after)) / (10 ** after)

    complete_num = before_num + after_num

    if negative:
        complete_num *= -1

    return complete_num

print(before_after(12345.678901, 1, 4))
print(before_after(12345.678901, 2, 3))
print(before_after(12345.678901, 3, 2))
print(before_after(12345.678901, 4, 1))

print(before_after(-12345.678901, 1, 4))
print(before_after(-12345.678901, 2, 3))
print(before_after(-12345.678901, 3, 2))
print(before_after(-12345.678901, 4, 1))
