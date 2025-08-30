def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]


input_text = input("Enter the string: ")

if is_palindrome(input_text):
    print("Is a palindrome")
else:
    print("NOT a palindrome")
