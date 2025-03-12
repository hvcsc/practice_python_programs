#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.6 - FIRST MINUS ALL
#DATE: MARCH 12, 2025


"""Prog06: Create a program that ask user to input 10 numbers.
Print the result of the first number minus all of the remaining numbers."""

#ask user for numbers
num1 = float(input("Enter the first number: "))

#sum of second to last number
num2 = 0
for i in range(9):
    num2 += float(input(f"Enter number {i + 2}: "))

#equation
#print output
