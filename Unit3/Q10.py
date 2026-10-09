# Write a program to extract specific information from a text file using regular expressions.
# it generate error please chek

import re

# Read data from a text file

with open("data.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone numbers
phones = re.findall(r'\b\d{10}\b', text)

# Display extracted information

print("Email addresses:", emails)
print("Phone numbers:", phones)
