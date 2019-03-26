
n = int(input("Please enter a positive number: "))
print(n)
def collatz(n): # function that will take in a number
    while n != 1: # Loop continues as long as n is not equal to 1. Once n is equal to 1 the loop stops!
        
        if n % 2 == 0:  # Check if the number is even (no remainder when divided to 2)
            n = n // 2
            yield(n)

        else: # If a number is not even then it must be odd. # elif n % 2 != 0: is anther way you can say this but is just mre verbose
            n = 3 * n + 1 # Current value of n multiply it by 3 and add 1.
            yield(n) # return the value 
            

print(collatz(n))

# explains yield https://stackoverflow.com/questions/33324432/collatz-sequence-python-3