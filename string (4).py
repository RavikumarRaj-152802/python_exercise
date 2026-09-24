#(4) Write a python program to print as following :
#Input : Hi
#Output : HHii
'''
val = input("enter hi :-")
print("output = "+"H",val+"i")
'''
string = input("Enter a string: ")

for ch in string:
    print(ch * 2, end="")