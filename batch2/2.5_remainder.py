#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.5 - REMAINDER
#DATE: MARCH 12, 2025

"""Prog05: Create a program that ask user to input 2 numbers.
Print the remainder when the first number is divided by the second number."""

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

#remainder equation
remainder = num1 % num2

#print remainder
print(f"\nThe remainder when {num1} is divided by {num2} is {remainder}")