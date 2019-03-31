'''
Roisin Fallon, 20 March 2019

Write a program that takes a positive ﬂoating point number as input and outputs an approximation of its square root. 
$ python squareroot.py 
Please enter a positive number: 14.5 

Approximate a square root of a floating point number
Adopted from (https://tour.golang.org/flowcontrol/8)
'''

while True:                                                                                             # While loop is used to deal with possible errors that arise as a result of an incorrect user input 
    try:
        n =float(input("Please enter a positive floating point number: "))                              # Asks the user to input a positive floating point number
    except ValueError:                                                  
        print("You have not entered a valid value. Try Again!")                                         # The user has not entered a valid number (e.g. letter). Thus, it prints the following statement.
        continue                                                                                        # The loop starts again, prompts user to enter a positive number
    if n < 0:                                                                                           # If the user inputs a negative number
        print("Sorry, you cannot get the square root of a negative number. Try again!.")                # Prompts the user that they have entered a negative number 
        continue                                                                                        # The loop starts again, prompts user to enter a positive number
    else:                                                                                               # User has given a valid number 
        break                                                                                           # Break- exits the while loop

import math                                                                                             # Import the math module  
print("The square root of", n, "is approx.", round(math.sqrt(n),1))                                     # Print the square root of the number the user inputted to 1 decimal place.  
                                                                                                        # sqrt() function is an inbuilt function in Python programming language - returns the square root of any number. 

'''

# Another method which will achieve the same result, this was proposed as an alternative approach in the Programming and Scripting Lecture.  

rootof = float(input("Please enter a positive number: "))                                                # Ask the user for a positive number that you are looking for the square root of
estimate = float(input("Please enter a initial estimate: "))                                             # Ask the user for an initial estimate of the square root
while abs((estimate * estimate) - rootof) > 0.1:                                                         # The while loop is repeated until the square of estimate is within 0.1 of root.
    estimate -= ((estimate * estimate ) - rootof)/ (2 * estimate)                                        # This is Newton's method to improve our estimate 
print(round(estimate),1)
print(f"The square root of {rootof} is approx.{estimate}.")                                              # Print the result
'''
