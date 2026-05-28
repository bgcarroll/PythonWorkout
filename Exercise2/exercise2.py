

def my_sum(*args):

    total = 0
    for arg in args:
        total += arg

    return total

print(my_sum(1, 2, 3))
print(my_sum(5,10,1,1,1,1,1))
print(my_sum(8,8,8,-8,8,-8,8,-8,8,8))
print(my_sum(-1, -2, 0, 3))