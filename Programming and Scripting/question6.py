'''
Roisin Fallon 18 March 2019

Write a program that takes a user input string and outputs every second word. 
$ python secondstring.py 
Please enter a sentence: The quick brown fox jumps over the lazy dog. 
The brown jumps the dog

Adapted from http://www.pitt.edu/~naraehan/python3/split_join.html
Adapted to remove full stops and commas https://stackoverflow.com/a/3559576
'''

x = (input('Please enter a sentence: '))            # Request to user to input a sentence
x = x.replace(',', '')                              # removes commas in the sentene entered by the user
x = x.replace('.', '')                              # removes full stops in the sentene entered by the user

everytwo = ' '.join(x.split()[::2])                 # .split() method returns a list of strings after breaking the given string by the specified separator.
                                                 # Join is used to put the list of words back together in a single string with a space in between (' ')
                                                # [start position: length of string: sequence]. in this instance i am using the default for the first 2 and 2 for the last one as I am looking for every second word. 
print(everytwo)                                             # Prints every second word 

# It was necessary to remove the full stop from the sentence in the example given in the question. 
# I also removed commas from the sentence as it is another common punctuation included in sentences. 