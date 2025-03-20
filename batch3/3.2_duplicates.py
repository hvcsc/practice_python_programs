"""Prog02: Create a program that ask user to input 10 numbers. Display all numbers.
For numbers with duplicate, display only the first entry."""

#define function
#create empty lists
def first_unique():
    user_input = []
    display_num = []

#ask for numbers then add to list
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        user_input.append(num)

#add occurrence to list
    for num in user_input:
        if num not in display_num:
            display_num.append(num)

#print output
    print(f"\nNumber list: {display_num}")

#call function
first_unique()
