"""Prog03: Create a program that ask user to input a number, continue asking
until the user input is invalid. Display "Unique" after input
when the inputted number don't have duplicate.
Display "Duplicate" after input when the inputted number have duplicate."""

#define function
#restrict non-numerical input
#create an empty list
def digit():
    number = []
    #ask for numbers
    while True:
        try:
            num = int(input("\nEnter a number: "))
            #check if the input is in the list
            if num in number:
                print("Duplicate.")
            else:
                print("Unique.")
                number.append(num)
        except ValueError:
            print("Invalid input.")
            break

#introduce the program
print("This program allows the user to input numbers repeatedly until a non-numerical value is entered.")

#call function
digit()

