#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1.5 - QUOTIENT
#DATE: MARCH 12, 2025

"""Prog05: Create a program that ask user to input 2 numbers.
Print the quotient of the two numbers with the decimal point"""

#restrict zero denominator
def zero(prompt):
    while True:
        num = float(input(prompt))
        if num == 0:
            print("Denominator cannot be zero.")
        else:
            return num

#ask user for numbers
num1 = float(input("Enter the first number: "))
num2 = zero("Enter the second number: ")

#quotient equation
quotient = num1 / num2

#print quotient