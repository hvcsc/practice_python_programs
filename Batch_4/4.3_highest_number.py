"""Prog03: Create a program that ask user to input a number,
continue asking until the user input is invalid. Display the highest number"""

#define function
#create an empty list
def highest_num():
    highest = None

    #ask for numbers
    while True:
        try:
            num = int(input("Enter a number: "))
            #store first input as the highest
            if highest is None:
                highest = num
            #check if input is higher than the current highest
            elif num > highest:
                highest = num
        except ValueError:
            break

    #print output
    if highest is None:
        print("\nNo numerical value entered.")
    else:
        print(f"\nHighest number: {highest}")
        
#introduce the program
#call function