#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.10 - IN BETWEEN
#DATE: MARCH 13, 2025

"""Prog10: Create a program that ask user to input 2 numbers.
Print all the numbers between the two numbers."""

#input numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#conditions and print
print(f"\nNumbers in between of {num1} and {num2}: ")
if num1 < num2:
    for num in range(num1 + 1, num2):
        print(num, end=" ")
elif num1 > num2:
    for num in range (num1 - 1, num2, -1):
        print(num,end=" ")
else:
    print("No numbers in between.")