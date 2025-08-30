sentence = input("Enter the sentence: ")

# split the sentence into words
words = sentence.split()

# init dictionary
word_count = {}

# count the word frequency
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
