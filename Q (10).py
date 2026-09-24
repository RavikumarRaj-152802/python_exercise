#Q (10).Write python programs to Print following Loops :

#a. 1 2 3 4 …… 10

for i in range(1, 11):
    print(i, end=" ")

# b. 2 4 6 ……. 20

for i in range(2, 21, 2):
    print(i, end=" ")

#c. 1 3 5 7 …… 19

for i in range(1, 20, 2):
    print(i, end=" ")

#d. 100 99 98…… 90

for i in range(100, 89, -1):
    print(i, end=" ")

#e. 200 198 196 …. 180

for i in range(200, 179, -2):
    print(i, end=" ")

#f. 0 1 1 2 3 5 8 ….. n

n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#g. 1 + 2 + …… + 10 = ans

ans = 0

for i in range(1, 11):
    ans = ans + i

print("1 + 2 + ... + 10 =", ans)

#h. ½ + 2/3 + ¾ …… + 9/10 = ans

ans = 0

for i in range(1, 10):
    ans = ans + i / (i + 1)

print("Answer =", ans)

#i. 1/10 + 2/20 ….. 10/100 = ans

ans = 0

for i in range(1, 11):
    ans = ans + i / (i * 10)

print("Answer =", ans)