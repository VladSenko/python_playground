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


# Tupples
colors = ("red", "green", "blue")  # can not be modified

single_item = ("glass",)  # a single item Tuple should end with a comma

print(colors[0])
print(colors[-1])


# Dictionaries

student = {"name": "Alice", "age": 25, "smokes": True}
print(student)
print(student["name"])  # dictionary property access

# modify and update dictionary
student["subject"] = "Math"
print(student)

student["age"] = 30
print(student)

del student["smokes"]
print(student)

student.pop("subject")
print(student)


# Dictionary iteration
for key, value in student.items():
    print(key, value)


# SETS - unordered collection of UNIQUE items (no duplicates)

nums = {1, 2, 3, 4}

empty_set = set()

# adding and removing items to set
nums.add(5)
print(nums)

nums.remove(2)
print(nums)


# Set operations: UNION, INTERSECTION, DIFFERENCE

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

print(set_1 | set_2)  # union
print(set_1 & set_2)  # intersection
# difference - checks what does not exist in set_2 that exists in set_1
print(set_1 - set_2)
