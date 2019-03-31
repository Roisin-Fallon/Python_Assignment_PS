'''
Roisin Fallon 26 February 2019

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
At each step calculate the next value by taking the current value and, if it is even, divide it by two,
but if it is odd, multiply it by three and add one. Have the program end if the current value is one. 
$ python collatz.py 
Please enter a positive integer: 10 
10 5 16 8 4 2 1

Adopted from https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
Other sources used are included in the README file. 
'''

while True:                                                             # while loop is used to deal with possible user input problems 
    try:
        n =int(input("Please enter a positive integer: "))              # Asks the user to input a positive number
    except ValueError:                                                  
        print("You have not entered a valid value. Try Again!.")        # The user has not entered a valid number (e.g. letter). Thus, it prints the following statement.
        continue                                                        # The loop starts again, prompts user to enter a positive number). 

    if n < 0:                                                           # If the user inputs a negative number
        print("Sorry, you must enter a positive integer.")              # It will print this statement to tell the user they have not met the requirement to enter a positive number.                                  
        
        continue                                                        # The loop starts again, prompts user to enter a positive number). 
    else:                                                               # User has given a valid number 
        break                                                           # Break- exit the loop
       
def collatz(n):                                                         # defines function that will take in a positive integer(n).
    while n > 1:                                                        # Loop continues as long as n is not equal to 1. Once n is equal to 1 the loop stops! end = " " is used to print the sequence of numbers to the same line
        print(n, end = " ")
        if n % 2 == 0:                                                  # Check if the number is even (no remainder when divided to 2)
            n = n // 2                                                  # As the number is even the condition is to divide the number by 2. // floor division used to restrict numbers to integers 
        else:                                                           # If the n is not divisible by 2 (i.e. n is odd)
            n = 3 * n + 1     	                                        # Current value of n multiply it by 3 and add 1.
   
    else:                                                          
        print(n)                                                        # prints the number 1
        print('Collatz sequence is now complete!')  	                # Informs the user the collatz sequence is finished. 
 
collatz(n)                                                              # calls the function 
