#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1.7 - SUMMATION
#DATE: MARCH 12, 2025


"""Prog07: Create a program that ask user to input 10 numbers.
Print the sum of all the numbers."""

#ask user for numbers
#add all numbers
summation = 0
for i in range(10):
    summation += float(input(f"Enter number {i + 1}: "))

#print summation
print(f"\nSummation of all given numbers:{summation: .2f}")