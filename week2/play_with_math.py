import math


def log(x):
    return math.log(math.sqrt(math.pow(x, 7)), 5)

print(log(5))
print(round(math.pi, 5))

row = 2
col = 3
nested_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print nested_list[row][col]