#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.1 - PRINT SMALLER NUMBER
#DATE: MARCH 12, 2025

"""Prog01: Create a program that ask user to input 2 numbers. Print the smaller number."""

#ask user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#check which is smaller
#print smaller number
if num1 < num2:
    print(f"\n{num1} is smaller than {num2}")
elif num2 < num1:
    print(f"\n{num2} is smaller than {num1}")