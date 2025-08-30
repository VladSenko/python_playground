import re


def clean_Text(text):
    # remove punctuation
    text = re.sub(f"[^\w\s]", "", text)

    # remove extra spaces
    text = " ".join(text.split())

    # convert to lower case

    return text.lower()


input_text = "     Hello, World! Welcome to Python...."

cleaned_text = clean_Text(input_text)
print(cleaned_text)
