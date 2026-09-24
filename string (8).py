"""
(8) Write a python program to enter a string from keyboard and count number of Vowels and No.
of consonants. Also give percentage of both.
"""

string = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():
        
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

total = vowels + consonants

vowel_percentage = (vowels / total) * 100
consonant_percentage = (consonants / total) * 100

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)

print("Percentage of Vowels:", vowel_percentage, "%")
print("Percentage of Consonants:", consonant_percentage, "%")