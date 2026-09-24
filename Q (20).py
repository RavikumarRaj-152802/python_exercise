# Q.20 Write a Python Program to perform 3x3 matrix multiplication.

print("Enter elements of Matrix A:")
A = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"A[{i}][{j}] = ")))
    A.append(row)

# Enter second 3x3 matrix
print("Enter elements of Matrix B:")

B = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)

# Matrix multiplication
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

# Display result
print("Resultant Matrix:")
for i in range(3):
    for j in range(3):
        print(C[i][j], end=" ")
    print()