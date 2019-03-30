''' 
Roisin Fallon 20 Feb 2019

Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
#$ python sumupto.py 
# Please enter a positive integer: 10 
# 55

Adopted from Lecture Material
'''

while True:                                                             # while loop is used to deal with possible user input problems 
    try:
        n =int(input("Please enter a positive integer: "))              # Asks the user to input a positive number
    except ValueError:                                                  
        print("You have not entered a valid value. Try Again!.")        # The user has not entered a valid number (e.g. letter). Thus, it prints the following statement.
        continue                                                        # The loop starts again, prompts user to enter a positive number. 

    if n < 0:                                                           # If the user inputs a negative number
        print("Sorry, you must enter a positive integer.")              # Prompts the user that they have entered a negative number 
        continue
    else:                                                               # User has given a valid number 
        break                                                           # Break- exit the loop


sum = 0                                                                 # Declare variable (this keeps track of all the positive numbers being added)      
while(n > 0):					                                        # Use while loop to iterate until it reaches 1. 
      sum += n 				 	                                        # Add the sum to the number entered by the user 
      n -= 1 						                                    # Deduct one from the value entered by the user, and go back to the top of loop.
      
print("Sum of all positive numbers is ", sum)                           # Displays the result to the user
