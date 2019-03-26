#Read the input from the user. Refer TO BREAK AND CONTINUE NOTES!!

n = int(input("Please enter a positive integer: "))

# Loop through the numbers 2(including 2) up to and including n (user input)
for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

else:
        # loop fell through without finding a factor which makes it a prime number!!
        print(n, 'is a prime number')