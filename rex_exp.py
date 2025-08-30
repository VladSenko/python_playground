import re

text = "Contact me at 123-456-7890"

# find all
digits = re.findall(r"\d+", text)
print(digits)

# replace
updated_text = re.sub(r"\d", "*", text)
print(updated_text)
