"""
Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of
the odd-indexed numbers. So, calling the function as even_odd_sums([10, 20,
30, 40, 50, 60]), you’ll get back [90, 120].
"""

def even_odd(nums):
    return [sum(nums[0::2]), sum(nums[1::2])]

print(even_odd([10, 20, 30, 40, 50, 60]))
print(even_odd((10, 20, 30, 40, 50, 60)))
