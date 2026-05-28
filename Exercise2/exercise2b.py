

def my_sum(args, base):

    total = base
    for arg in args:
        total += arg

    return total

print(my_sum([1, 2, 3], 5))
print(my_sum([5,10,1,1,1,1,1], -10))
print(my_sum([8,8,8,-8,8,-8,8,-8,8,8], 0))
print(my_sum([-1, -2, 0, 3], 4))
