"""Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number
from lowest to highest. Clue: sort() function"""

#define function
#create an empty list
def ascending():
    numbers = []

    #ask for numbers then add to list
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            break

    #sort and print numbers
    if numbers:
        numbers.sort()
        print(f"\nNumbers in ascending order: {numbers}")
    else:
        print("No numerical value entered.")

#introduce program
#call function