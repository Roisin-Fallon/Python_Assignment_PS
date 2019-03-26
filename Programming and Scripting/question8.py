
# Reference https://docs.python.org/2/library/datetime.html

import datetime as dt

# Current date and time.
print(dt.datetime.strftime(dt.datetime.now(), "%A, %B %d %Y at %I:%M %p"))


def S(self):
    
    if self.data.day in (11, 12, 13):  # Special case
        return 'th'
    last = self.data.day % 10
    if last == 1:
        return 'st'
    if last == 2:
        return 'nd'
    if last == 3:
        return 'rd'
    return 'th'

#def date_suffix():
   # if %d in [1, 21, 31]: 
    #    suffix = 'st'
    #elif %d in [2, 22]:
     #   suffix = 'nd'
    #elif %d in [3, 23, 33]:
     #   suffix = 'rd'
    #else:
     #   suffix = 'th'