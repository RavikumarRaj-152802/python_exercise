#(3) Write a python program to enter a string and check whether it is palindrome or not ?

string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")