''' 
Roisin Fallon, 28 Feb 2019

Write a program that outputs whether or not today is a day that begins with the letter T. 

An example of running this program on a Thursday is as follows. 
$ python begins-with-t.py
 Yes - today begins with a T.

An example of running it on a Wednesday is as follows. 
$ python begins-with-t.py 
No - today does not begin with a T.

Adapted from Lecture Material: https://github.com/ianmcloughlin/python-tuesday/blob/master/tuesday.py
'''

import datetime                                    # Import the datetime module 
if datetime.datetime.now().weekday() in [1, 3]:    # Checks to see if the day is Tuesday or Thursday.
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.") 	   # The remainder of days in the week do not begin with T. 
