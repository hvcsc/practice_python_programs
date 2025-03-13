"""Prog01: Create a program that ask user to input 10 numbers.
Display all numbers that don't have duplicate."""

#define unique numbers
#create an empty list
def unique():
    user_input = []

#ask for numbers and add to the list
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        #add to the list
        user_input.append(num)

#create an empty list for unique numbers
#count number occurrences then add to the unique list
#print unique numbers