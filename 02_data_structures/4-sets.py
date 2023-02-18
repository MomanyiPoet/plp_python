#!/usr/bin/python3

# declare two empty sets
a_set = set()
b_set = set()

# user to input two intergers for set a_set
print("Set A Intergers: ")
for a in range(3):
    A = int(input("Enter Interger: "))
    a_set.add(A)

# user to input two intergers for set b_set
print("Set B Intergers: ")
for b in range(3):
    B = int(input("Enter Interger: "))
    b_set.add(B)

intersect = a_set & b_set

if not intersect:
    print("No common elements")
else:
    for x in intersect:
        print(f"Common Elements: {x}")
