'''
Roisin Fallon 18 March 2019

Write a program that takes a user input string and outputs every second word. 
$ python secondstring.py 
Please enter a sentence: The quick brown fox jumps over the lazy dog. 
The brown jumps the dog

Adapted from https://stackoverflow.com/a/509295; http://www.pitt.edu/~naraehan/python3/split_join.html
Adapted to remove full stops and commas https://stackoverflow.com/a/3559576
'''

x = (input('Please enter a sentence: '))                   # Request to user to input a sentence
x = x.replace(',', '')                                     # Removes commas in the sentene entered by the user
x = x.replace('.', '')                                     # Removes full stops in the sentene entered by the user

everytwo = ' '.join(x.split()[::2])                        # .split() method returns a list of strings after breaking the given string by the specified separator.
                                                           # [start: stop: step] * This is explained further below
                                                           # Join is used to put the list of words back together in a single string with a space in between (' ')
                                                            

print(everytwo)                                             # Prints every second word 

# It was necessary to remove the full stop from the sentence in the example given in the question. 
# I also removed commas from the sentence as it is another common punctuation included in sentences. 

# [start: stop: step] start is what the position to start. In this instance I have entered no value so it will default to position zero.
# stop refers to what position on the string you want to finish. Again because I want the full string to be included I will use the default value.
# step refers to increments i.e. if you want every second word it would be 2. 
