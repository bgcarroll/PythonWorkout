
def my_avg(numbers):
    return sum(numbers) / len(numbers)

def my_avg2(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def my_avg3(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(my_avg([1,2,3,7]))
print(my_avg2([1,2,3,7]))
