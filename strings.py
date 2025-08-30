# concatenation
import re
first = "Hello"
secont = "World"

result = first + " " + secont

print(result)


# slicing
text = "Python Programming"
print(text[0:6])
print(text[-11:])


# formating
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# Common string methods

# split()

sentence = " Python  is fun"
words = sentence.split()
print(words)

# join
new_sentence = " ".join(words)
print(new_sentence)


# replace
text = "I love Java"
updated_text = text.replace("Java", "Python")
print(updated_text)

messy = "     Hello World.   "
cleande_text = messy.strip()
print(cleande_text)
