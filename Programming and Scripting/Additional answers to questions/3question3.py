
# To get numbers between 1000 and 10000 we use the range function 

for x in range(100, 10000):


# To determine if they are divisible by 6 and not divisible by 12
    if (x % 6 == 0 and x % 12 != 0):

# To format the numbers with , where necessary  
       print(f"{x:,d}")
   