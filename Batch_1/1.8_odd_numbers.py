#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1.8 - ODD NUMBERS COUNT
#DATE: MARCH 12, 2025

"""Prog08: Create a program that ask user to input 10 numbers.
Print how many are odd numbers."""

count = 0
#ask user for numbers
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    #check for odd numbers
    #initialize and count how many odd numbers
    if num % 2 != 0:
        count += 1

#print output
print(f"\nThere is/are {count} odd number/s.")