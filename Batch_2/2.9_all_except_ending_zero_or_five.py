#AUTHOR: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 2.9 - ALL EXCEPT ENDING IN ZERO OR FIVE
#DATE: MARCH 12, 2025

"""Prog09: Create a program that print all the numbers
starting from 0 to 100 except numbers ending in zero or ending five."""

#set for loop and condition
for num in range(101):
    if num % 10 != 0:
        if num % 10 != 5:
            #print output
            print(num)
