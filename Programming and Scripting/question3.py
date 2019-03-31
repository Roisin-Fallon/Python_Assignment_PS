'''
Roisin Fallon 20 Feb 2019 

Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 
$ python divisors.py 
1002 
1014 
1026 etc 
9990

Format adopted from: https://stackoverflow.com/a/45367591 (used to include commas when numbers are in there thousands)
'''

for x in range(1000, 10001): 		# x increases by 1 each time it loops, it starts at 1000 and ends 10001 (explanation of why below)
    if (x % 6 == 0 and x % 12 != 0): 	# To determine if they are divisible by 6 and not divisible by 12
       print(f"{x:,d}") 			# Format numbers with commas. This line can be omitted from the code without affecting the code.
  
        
# In this question they ask for the numbers between 1000 and 10000, in using the Python compiler (link in README) I noticed the 
# last number than ran through the for loop was 9999 which is 1 less than the question requested. On further research I realised that the range(n) 
# is of exclusive nature and hence will not include last number (10000) in the output. 
# To rectify this I increased 10000 by 1 which gave me a new range of (1000, 10001). Adapted from https://pynative.com/python-range-function/ ''''
