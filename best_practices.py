# [expressions for in iterable if condition]

# squares = [x**2 for x in range(10)]
# print(squares)


# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)


# Lambda functions
# add = lambda x, y: x + y

# print(add(3,5))

from functools import reduce
numbers = [1, 2, 3, 4]

# map
squares = map(lambda x: x**2, numbers)
print(list(squares))

# filter
evenList = filter(lambda x: x % 2 == 0, numbers)
print(list(evenList))

# reduce
product = reduce(lambda x, y: x*y, numbers)
print(product)
