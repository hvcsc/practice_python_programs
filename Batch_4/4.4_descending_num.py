"""Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid.
Display the number from highest to lowest. Clue: sort() function"""

#define function
#create an empty list
def descending():
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
        numbers.sort(reverse=True)
        print(f"\nNumbers in descending order: {numbers}")
    else:
        print("No numerical value entered.")

#introduce program
print("This program continuously accepts numerical inputs until a "
      "non-numerical value is entered, then displays the numbers in descending order.")

#call function
descending()