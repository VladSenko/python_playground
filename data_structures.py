# List

numbers = [1, 2, 3, 4, 5]

fruits = ['apples', 'banana', 'oranges']

mixed = [1, True, 'apple']

print(numbers[2])
print(fruits[-1])  # the last item of list

fruits.append('cherry')
fruits.insert(1, 'grape')  # insert an item to specified index

print(fruits)

# get sublist of items starting on the startIndex and ending BEFORE the endIndex
sliced_fruits = fruits[1:3]
print('Sliced fruits', sliced_fruits)

fruits.remove("banana")  # remove an item from the list

print(fruits)

del fruits[0]  # remove an item at specified index
print(fruits)

fruits.pop()  # remove the last item from the list
print(fruits)
