#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1.1 - PRINT BIGGER NUMBER
#DATE: MARCH 12, 2025

"""Prog01: Create a program that ask user to input 2 numbers.
Print the bigger number."""

#ask user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#check which is bigger
#print output
if num1 > num2:
    print(f"\n{num1} is bigger than {num2}")
elif num2 > num1:
    print(f"\n{num2} is bigger than {num1}")
