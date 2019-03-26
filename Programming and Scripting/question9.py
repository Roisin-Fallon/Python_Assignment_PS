# Adapted from


with open("C:\\test.txt", 'r') as f:

# This is to start at line of the code 
    for count, line in enumerate(f, start=1):

        if count % 2 == 0:
            print(line)