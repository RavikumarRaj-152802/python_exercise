#Q (10).Write python programs to Print following Loops :

#a. 1 2 3 4 …… 10

print("Output of a :-")

for i in range(1, 11):
    print(i, end=" \n")

# b. 2 4 6 ……. 20

print("Output of b :-")

for i in range(2, 21, 2):
    print(i, end=" \n")

#c. 1 3 5 7 …… 19

print("Output of c :-")

for i in range(1, 20, 2):
    print(i, end=" \n")

#d. 100 99 98…… 90

print("Output of d :-")

for i in range(100, 89, -1):
    print(i, end=" \n")

#e. 200 198 196 …. 180

print("Output of e :-")

for i in range(200, 179, -2):
    print(i, end=" \n")

#f. 0 1 1 2 3 5 8 ….. n

print("Output of f :-")

n = int(input("Enter num: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" \n")
    a, b = b, a + b

#g. 1 + 2 + …… + 10 = ans

ans = 0

for i in range(1, 11):
    ans = ans + i

print("Q(g).1 + 2 + ... + 10 =", ans)

#h. ½ + 2/3 + ¾ …… + 9/10 = ans

ans = 0

for i in range(1, 10):
    ans = ans + i / (i + 1)

print("Answer of Q.h =", ans)

#i. 1/10 + 2/20 ….. 10/100 = ans

ans = 0

for i in range(1, 11):
    ans = ans + i / (i * 10)

print("Answer of Q.i =", ans)
