#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1.6 - EXPONENT
#DATE: MARCH 12, 2025

"""Prog06: Create a program that ask user to input 2 numbers.
Print the result when the first number is raised to the second number."""

#ask user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#power equation
power = num1**num2

#print output
print(f"\n{num1} raised to {num2} is{power: .2f}")