# Q.6. Write a program to illustrate the use of tuples and sets with basic operations.

# Creating a tuple

t = (10, 20, 30, 40, 50)
print("Original Tuple:", t)

# Tuple operations

print("First Element:", t[0])
print("Last Element:", t[-1])

print("Tuple Slicing:", t[1:4])
print("Length of Tuple:", len(t))

print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Creating sets

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("\nSet A:", a)
print("Set B:", b)

# Set operations

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))

# Adding and removing elements

a.add(50)
print("After Adding 50:", a)

a.remove(20)
print("After Removing 20:", a)