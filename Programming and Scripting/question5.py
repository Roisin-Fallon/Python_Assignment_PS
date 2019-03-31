'''
Roisin Fallon 04 March 2019

Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
$ python primes.py 
Please enter a positive integer: 19 
That is a prime.
Adapted from Lecture material for Programming and Scripting (Break and Continue)
Adapted from https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
'''

while True:                                                                                    # while loop is used to deal with possible inputs that may cause an error 
    try:
        n =int(input("Please enter a positive integer: "))                                     # Asks the user to input a positive integer. 
    
    except ValueError:                                                  
        print("You have not entered a valid integer. Try Again!.")                             # The user has not entered a valid number (e.g. letter). Thus, it prints the following statement.
        continue                                                                               # The loop starts again, prompts user to enter a positive integer. 

    if n < 1:                                                                                  # If the user inputs a negative number or zero. 
        print("Prime numbers are integers greater than 1. Try Again!.")                        # Prompts the user that they have must give a number > 1
        continue                                                                               # The loop starts again, prompts user to enter a positive integer.
    else:                                                                                      # User has given a valid number 
        break                                                                                  # Break- exit the loop

if n == 1:                                                                                     # As n is by definition not a prime number. If statement added to state this. 
        print(n, 'is not a prime number')  
else:
        for x in range(2, n):                                                                  # Loop through the numbers 2 (including 2) up to and including n (user input).
                if n % x == 0:                                                                 # Determine if n has a factor  i.e. is the number divisible by any number other than 1 and itself.                     
                        print("This is not a prime number as", n,  "has a factor of", n//x)    # Displayed to user
                        break                                                                  # Breaks -exits the inner for loop as it does not need to determine all the factors as this not what the algorithm is looking for.
                                                                  
        else:
                print(n, 'is a prime number')                                                  # Loop fell through without finding a factor which makes it a prime number!!

