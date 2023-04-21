#!/usr/bin/python3

divisible_by_ten = lambda num: True if num % 10 == 0 else False

print("Is your number divisible by Ten")
num = int(input("Enter a number "))

print(divisible_by_ten(num))