"""Prog05: Create a program that ask user to input a number, continue asking
until the user input is invalid. Display the average."""

#define function
#create and empty list
#initialize
def calc_ave():
    numbers = []
    count = 0

    #ask for numbers
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
            count += 1
        except ValueError:
            break

    #calculate average and print
    if count > 0:
        total_sum = sum(numbers)
        average = total_sum / count
        print(f"\nAverage: {average: .2f}")
    else:
        print("No numerical value entered.")

#introduce program
#call function