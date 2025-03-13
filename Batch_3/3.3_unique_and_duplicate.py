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
            num = int(input("Enter a number: "))
            #check if the input is in the list
            if num in digit:
                print("Duplicate.")
            else:
                print("Unique.")
                number.append(num)
        except ValueError:
            print("Invalid input.")
            break
            
#introduce the program
#call function

