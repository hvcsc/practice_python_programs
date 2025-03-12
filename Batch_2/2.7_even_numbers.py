#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.7 - EVEN NUMBERS COUNT
#DATE: MARCH 12, 2025

"""Prog07: Create a program that ask user to input 10 numbers.
Print how many are even numbers."""

count = 0
#ask user for numbers
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    # check for even numbers
    # initialize and count how many even numbers
    if num % 2 == 0:
        count += 1

#print output