"""Prog04: Create a program that ask user to input a number, continue asking
until the user input is invalid. Display the lowest number"""

#define function
#create an empty list to store inputs
def lowest_num():
    lowest = None

    #ask for numbers
    while True:
        try:
            num = int(input("Enter a number: "))
            #store input to lost
            if lowest is None:
                lowest = num
            #check if input is lower than the number in the list
            elif num < lowest:
                lowest = num
        except ValueError:
            break

#print output
#call function