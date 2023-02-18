#!/usr/bin/python3

# initialize an empty list
int_list = []

# Get input from user for 5 integers and append them to the empty list
for i in range(5):
    integ = int(input("Enter an interger: "))
    int_list.append(integ)

# compute sum of items in list using sum() function
list_sum = sum(int_list)

#output sum
print(f"Sum is: {list_sum}")
