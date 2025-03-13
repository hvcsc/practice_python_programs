"""Prog01: Create a program that ask user to input 10 numbers.
Display all numbers that have duplicate."""

#define function
#create empty lists
def duplicates():
    numbers = []
    dups = []

    #ask for numbers then add to list
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"\nEnter number {i + 1}: "))
        numbers.append(num)

    #check duplicates and add to lost
    for num in numbers:
        count = numbers.count(num)
        if count > 1:
            if num not in dups:
                dups.append(num)

    #print output
    if dups:
        print(f"\nNumber/s with duplicates: {dups}")
    else:
        print("\nNo duplicates.")

#introduce the program
#call function