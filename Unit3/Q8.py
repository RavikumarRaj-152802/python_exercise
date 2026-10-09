# Write a program to demonstrate basic regular expression pattern matching.

import re

text = "Python is easy. Python is powerful."

# 1. Search for a pattern

result = re.search("easy", text)
print("Search:", result.group() if result else "Not found")

# 2. Find all occurrences

result = re.findall("Python", text)
print("Find all:", result)

# 3. Match at the beginning

result = re.match("Python", text)
print("Match:", result.group() if result else "Not found")

# 4. Replace a pattern

result = re.sub("Python", "Java", text)
print("Replace:", result)
