'''
Roisin Fallon 25 March 2019

Write a program that displays a plot of the functions x, x**2 and 2**x in the range [0,4].

Adapted from https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
Further references included in README
'''

import matplotlib.pyplot as plt                                                        # import matplotlib which is given an alias of plt. Alias is used to reference from now on.  
import numpy as np                                                                     # Import numpy which is given an alias of np. numpy is used to perform calculations

x = np.arange(0.0, 4.0, 0.1)                                                           # (a,b,c) a=start point b=end point c= evenly sampled every 0.1ms 
y1 = x                                                                                 # function x 
y2 = x*x                                                                               # function x^2 or could say y= x**2
y3 = 2**x                                                                              # function 2^x 

plt.plot(x, y1, color="purple", linewidth =2, linestyle="-", label = "x")              # Plot y=x, format the line created. 
plt.plot(x, y2, color="green", linewidth =2,  linestyle="--",  label = "x^2")          # Plot y= x^2),format the line created.
plt.plot(x, y3, color="blue", linewidth =2 , linestyle=":", label = "2^x")             # Plot f(2^x), format the line created.

# Formatting of the graph 

plt.xlabel('x - axis')                                                                 # naming the x axis 
plt.ylabel('y - axis')                                                                 # naming the y axis   
plt.title('Graphing Functions')                                                        # Add title to graph 
plt.grid(True)                                                                         # Add grid lines to the graph background
plt.legend(["y1 = x", "y2 = x^2", "y3 = 2^x"])                                         # Add legend to graph
plt.plot(1,1,'ro')                                                                     # Point of intersection of y1 and y2
plt.plot(2, 4, 'ro')                                                                   # Point of intersection of y2 and y3
plt.margins(0)                                                                         # By default, matplotlib adds a 5% margin on all sides of the axes. I wanted to remove this. 

plt.show()                                                                             # call to display the figure


