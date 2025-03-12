#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 10 - ALL NUMBERS FROM 0-100 EXCEPT ENDING IN ZERO
#DATE: MARCH 12, 2025

"""Prog10: Create a program that print all the numbers
starting from 0 to 100 except numbers ending in zero."""

#set loop and condition
for i in range(0, 101):
    if i % 10 != 0:
        #print output
        print(i)