def min_max(number):
    bigger = max(number)
    smaller = min(number)
    return (bigger, smaller)

result = min_max([5, 2, 3, 4, 6])
print(result)
