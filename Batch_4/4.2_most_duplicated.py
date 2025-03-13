"""Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid.
Display the number with the most number of duplicate."""

#define function
#create an empty dictionary
def most_dups():
    num_count = {}
    most_dupli = []
    max_count = 0

    #ask for numbers
    while True:
        try:
            num =int(input("Enter a number: "))
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        except ValueError:
            break

    #find the highest occurrence
    if num_count:
        max_count = max(num_count.values())

        for num in num_count:
            if num_count[num] == max_count:
                most_dupli.append(num)

    #print output
    print(f"Most duplicated number/s: {most_dupli}")

#introduce program
print("This program continuously accepts numerical inputs until a "
      "non-numerical value is entered, then displays the number(s) with the most duplicates.")

#call function
most_dups()
