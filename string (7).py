#(7) Write a python program to perform following operation :
#Input String : Hello
#Input a character : X
#Input number of times : 3
#Output : HelloXHelloXHello

string = input("Input String: ")
char = input("Input a character: ")
n = int(input("Input number of times: "))

output = (string + char) * n

print("Output:", output)