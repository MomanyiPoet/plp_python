#!/usr/bin/python3

# initialize empty dictionary
person = {}

# user inputs
name = str(input("What is your name? "))
person["Name"] = name

age = str(input("What is your age? "))
person["Age"] = age

favourite_col = str(input("What is your Favourite Color? "))
person["Favourite Color"] = favourite_col

# print to console
for i in person:
    print(i,":", person[i])