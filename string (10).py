"""
(10)Write a python program to count the digits in given string and also give sum of digits. If no digits
available in string print 0.
Input : Hello123World
Output : No. of digits : 3
         Sum of digits : 6
Input : HelloWorld
Output : 0
"""

string = input("Enter a string: ")

count = 0
sum_digits = 0

for ch in string:
    if ch.isdigit():
        count += 1
        sum_digits += int(ch)

if count == 0:
    print("0")
else:
    print("No. of digits:", count)
    print("Sum of digits:", sum_digits)