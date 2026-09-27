'''
Q.(17.1) Write Python Programs to print following triangles.
    1
    12
    123
    1234
    12345
    12345
    1234
    123
    12
    1
'''
print("output of Q17.1 :-")

# Print the increasing triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print the decreasing triangle
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

'''
Q.(17.2) Write Python Programs to print following triangles
1
21
321
4321
54321
54321
5432
543
54
5
'''
print("output of Q17.2 :-")

# Increasing triangle
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Decreasing triangle
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()

'''
Q.(17.3) Write Python Programs to print following triangles
5
45
345
2345
12345
54321
4321
321
21
1
'''
print("output of Q17.3 :-")

# First triangle
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end="")
    print()

# Second triangle
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

'''
Q.(17.4) Write Python Programs to print following triangles
12345
2345
345
45
5
1
23
456
78910
…… n
'''
print("output of Q17.4 :-")

for i in range(1, 6):
    for j in range(i, 6):
        print(j, end="")
    print()

n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end="")
        num += 1
    print()

'''
Q.(17.5) Write Python Programs to print following triangles
5
54
543
5432
54321
1
10
101
1010
10101
'''
print("output of Q17.5 :-")

for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(i):
        print((j + 1) % 2, end="")
    print()

'''
Q.(17.6) Write Python Programs to print following triangles
1
01
010
1010
10101
'''
print("output of Q17.6 :-")

for i in range(1, 6):
    start = 1 - (i // 2) % 2

    for j in range(i):
        print((start + j) % 2, end="")
    print()

'''
Q.(17.7) Write Python Programs to print following triangles
	    1
 	  2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''
print("output of Q17.7 :-")

for i in range(1, 6):

    # Print spaces
    for j in range(5 - i):
        print("  ", end="")

    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    # Print increasing numbers
    for j in range(2, i + 1):
        print(j, end=" ")

    print()

'''
Q.(17.8) Write Python Programs to print following triangles
*
**
***
****
*****
'''
print("output of Q17.8 :-")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

'''
Q.(17.9) Write Python Programs to print following triangles
    *
   **
  ***
 ****
*****
'''
print("output of Q17.9 :-")

for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print(" ", end="")

    # Print stars
    for j in range(i):
        print("*", end="")

    print()

'''
Q.(17.10) Write Python Programs to print following triangles
    *
   **
  ***
 ****
*****
'''
print("output of Q17.10 :-")
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)