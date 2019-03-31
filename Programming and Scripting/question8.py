'''
Roisin Fallon 20 March 2019

Write a program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 
Adapted from https://docs.python.org/3.4/library/datetime.html?highlight=weekday
'''

import datetime as dt                                                                               # import datetime module with an alias dt 
                                                                    
now = dt.datetime.now()                                                                             # To get the current date and time when the program is run 
date_string = now.strftime('%A, %B # %Y at %#I:%M%p')                                               # Detailed explanation of this is included in README 
month_date = now.day

if (3 < month_date< 21) or (23 < month_date < 31):                                                  # Created an if statement to deal with the suffix related to the month date.
  month_date = str(month_date) + 'th'                                                               # th is associated with with the days 
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  month_date = str(month_date) + suffixes[month_date % 10]                                          # Divide the day by 10, if you get a remainder of: 1 (st suffix); 2 (nd suffix); 3 (rd suffix)  

print(date_string.replace('#', month_date).replace('PM','pm').replace('AM','am'), end='')           # Print the current date and time in the desired format. 


