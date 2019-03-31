'''
Roisin Fallon 25 March 2019

Write a program that displays a plot of the functions x, x**2 and 2**x in the range [0,4].

Adapted from https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
Formating of graph adapted from https://matplotlib.org/2.0.2/api/lines_api.html; https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
'''

import matplotlib.pyplot as plt # import matplotlib which is given an alias of plt. Alias is used to reference from now on.  
import numpy as np # Import numpy which is given an alias of np. numpy is used to perform calculations

x = np.array([0,1,2,3,4])   
y1 = x       # function x 
y2 = x*x     # function x^2 or could say y= x**2
y3 = 2**x    # function 2^x 

plt.plot(x, y1, color="red", linewidth =2 , linestyle="-", label = "x") # Plot y=x, format the line created. 
plt.plot(x, y2, color="green", linewidth =3,  linestyle="--",  label = "x^2") # Plot y= x^2),format the line created.
plt.plot(x, y3, color="blue", linewidth =4 , linestyle=":", label = "2^x") # Plot f(2^x), format the line created.

# Formatting of the graph 
plt.xlabel('x - axis') # naming the x axis 
plt.ylabel('y - axis') # naming the y axis   
plt.title('Graphing Functions') # Add title to graph 

plt.legend(["y1 = x", "y2 = x^2", "y3 = 2^x"]) # Add legend to graph
plt.show()   # call to display the figure


