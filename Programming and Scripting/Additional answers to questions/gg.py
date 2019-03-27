
# Adopted from

n = input("Please enter a positive number: ")
print(n)

def collatz(n): # function that will take in a number
    if n % 2 == 0:  # Check if the number is even (no remainder when divided to 2)
            print(n // 2)
            return n // 2


    else n % 2 != 0:
            n = 3 * n + 1 # Current value of n multiply it by 3 and add 1.
            print(n)
            return n # return the value 
            
while n != 1: # Loop continues as long as n is not equal to 1. Once n is equal to 1 the loop stops!
    n = collatz(int(n))


        
   