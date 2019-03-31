'''
Roisin Fallon 20 March 2019
Write a program that reads in a text ﬁle and outputs every second line.
The program should take the ﬁlename from an argument on the command line. 
$ python second.py moby-dick.txt 
Title: Moby Dick; or The Whale CHAPTER 1 
Call me Ishmael. Some years ago--never mind how long 
particular to interest me on shore, I thought I would sail about a ...

Adapted from Programming and Scripting Lecture material
'''


import sys                                                             # sys library is imported this is required to use sys.argv

try:                                                                  # Try and except block helps catch and deal with exceptions.
    
    if len(sys.argv) == 2:                                             # len(sys.argv) function counts number of arguments supplied through command line. In this case we are looking for length of exactly two (script file and the single argument
        with open(sys.argv[1], 'r') as f:                              # With statement will open the text file (second element) as f.
            m = f.readlines()                                          # f.readline() reads a single line from the file assigned a variable m 
            for i in range(0, len(m), 2):                              # For loop starts at position 0 (1st line in txt); stops at len(m), full length of txt file; step refers to increments (every second line it would be 2).
                print(m[i], end='')                                    # print every second line, with end ='' to stop the newline
                         
    else:
        print ("You should supply a single text filename.")           # Prompts the user to check they have not entered more than one 
        sys.exit()                                                    # Exits the program immediately

except OSError:
    print("Please check the filename. Cannot open file!")             # Prompts the user to check the filename is correct
    sys.exit()                                                        # Exits the program immediately
