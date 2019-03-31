# Higher Diploma in Data Analytics 

## Module: Programming and Scripting 

### Problem Set: 

 

* This repository contains the 2019 Problem Set for the Programming and Scripting at GMIT.*

See instructions here: https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf


__Programs recommended to download before running the program:__

- anaconda on your device (version 3.7 +) 

 - Visual Studio Code 

- Cmder command line  


__How to access this repository__

Go to GitHub https://github.com/Roisin-Fallon/Python_Assignment_PS/tree/master/Programming%20and%20Scripting

Click the download button and save the zip file to your devise 

 

__File Contents__


__Question 1:__

This program asks the user to input a positive number and it will return the sum of all positive numbers between 1 and the number the user inputs. Example: If the user entered the number 10 it would return 55 to the user. 

In my solution I tried to cover a number of possible incorrect inputs that a user may enter and how the program should deal with it. For instance, if a letter or negative number was entered it will prompt the user that they have not fulfilled the requirements of the question (to input a positive integer).  Hence the while loop will run indefinitely (through the use of a continue statement) until a positive integer is entered. Once the user inputs a positive integer the break statement will break you out of the while loop instantaneously.  The use of continue and break statements alter the flow of a normal loop.  

While loop is used to solve the computation of the sum of the numbers. Each time it loops the condition is checked (num>0), if true it adds this num to the sum and it deducts one from the num. It returns back to the top of while loop and checks the condition again. It iterates through the loop until it reaches 1 it displays the result of the print statement to the user.  


*References:*

Lecture material from the Programming and Scripting module 

https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

 

__Question 2:__

This program is used to determine if the day begins with the letter T (Tuesday or Thursday).   

A module called datetime() is imported as Python does not have its own built in.   

An if statement was used to solve this problem. Tuesday is allocated the number 1 and Thursday is allocated the number 3, this is on the basis that Monday is 0 and so on up until Sunday which is assigned 6.  datetime.now() gives the current date and time and hence will return the result based on what day the user runs the program.  

*References:*

Lecture material from the Programming and Scripting module Week 2 

GitHub //github.com/ianmcloughlin/python-tuesday/blob/master/tuesday.py.

 

__Question3:__

A for loop was used in this question, x is a variable that increases by 1 every time it iterates through the loop starting at 1000 and finishing at 10001 (note not 10000). Using the python compiler (link included below), the range had to be modified slightly as the program ran up to 99999 and then ended. On further research I realized that the range(n) is of exclusive nature and hence will not include last number (10000) in the output. To rectify this, I increased 10000 by 1 which gave me a new range of (1000, 10001). 

To determine if the number is divisible by 6 and not by 12 we focus on presence of a remainder.  There should be no remainder when divided by 6 (x % 6 == 0.) There should be a remainder when divided by 12 (x % 12 != 0). To the result I have included a format function to this which includes commas where necessary this improves the readability of the program output e.g. 9,990 instead of 9999. 
 

*References:*

https://stackoverflow.com/a/45367591 

https://www.onlinegdb.com/online_python_compiler 

https://pynative.com/python-range-function/ 

 

__Question 4:__

Similar to Question 1, the validity of the user input was tested (Please refer to Question 1 for further explanation).   

Define function that will take in a positive integer(n) and will be used to calculate the collatz sequence. The collatz algorithm consists of a While loop with nested if and else statement. While loop relates to the condition that the calculation nested within will be performed as long as n is not equal to 1, hence it will continue to loop until the condition fails. If statement checks if the number is even and performs a calculation accordingly. If it is not even the number has to be odd hence else statement and perform a separate calculation for off numbers.  Each time the while loop condition is checked.  

Format function was added to ensure the sequence of numbers was printed on the same line using end = " ". 

It is important to understand that a collatz sequence will always reach 1 regardless of the natural number the user inputs. The length of the sequence of numbers does vary with the number the user entered.  

 
*Reference:*

https://www.tutorialspoint.com/python3/python3_whatisnew.html

https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ 

https://stackoverflow.com/questions/33324432/collatz-sequence-python-3

https://www.jasondavies.com/collatz-graph/ 


__Question 5:__

Before starting with this problem, it is important to understand what a prime number is. According to Collins dictionary: “a prime number is a whole number greater than 1 that cannot be divided exactly by any whole number except itself and the number 1”.  

Similar to Question 1, the validity of the user input was tested (Please refer to Question 1 for further explanation).  Upon running the code, I observed an additional statement was needed to deal with the number 1, as it initially it returned “1 is a prime number”.  To rectify this an if statement was added.  

Once a valid number has been entered it breaks from there while loop. This number then enters into a for loop which iterates through the numbers 2 (including 2) up to and including n (user input). It determines if n has a factor i.e. is it divisible by any number other than one and itself, with each loop x increases by 1. If a factor is found it breaks -exits the inner for loop as it does not need to determine all the factors as this not what the algorithm is looking for. The break statement saves time. In keeping with the definition above if we find any other number that is divisible other than it is not a prime number.  Else means that the loop fell through without finding a factor which makes it a prime number!! 


*Reference:*

 Lecture material for Programming and Scripting  

https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

https://www.collinsdictionary.com/dictionary/english/prime-number

 

__Question6:__

The user is prompted to enter a sentence and the output will be every second word. 

.split() method returns a list of strings after breaking the given string by the specified separator. As separator argument is absent, whitespace characters are replaced by a single space (also leading and trailing space is eliminated).  

Join is used to put the list of words back together in a single string with a space in between (‘ ’.join). 

[start: stop: step] start is what the position to start. In this instance I have entered no value so it will default to position zero. Stop refers to what position on the string you want to finish. Again, because I want the full string to be included I will use the default value. Step refers to increments i.e. if you want every second word it would be 2.  

It was necessary to remove the full stop from the sentence in the example given in the question. I also removed commas as it is another common punctuation that is often seen in sentences. 

 
*References: *

 http://www.pitt.edu/~naraehan/python3/split_join.html

 https://stackoverflow.com/a/3559576

 

__Question 7:__

Similar to Question 1, the validity of the user input was tested (Please refer to Question 1 for further explanation).  However, the main difference is this time the user is prompted to enter a floating point number (previous to this it was a positive integer). Math module is imported - sqrt() function is an inbuilt function in Python programming language - returns the square root of any number. The number was rounded to round decimal place as requested in the question.  

Within this solution I have included an approach that was referred to in the Programming and Scripting module lectures which uses a Newtons method to determine the square root (see below), where z refers to users estimate and x refers to the number we are look for the square root of.  

__z -= (z*z - x) / (2*z)__

Newton’s square root method prompts the user to first enter a positive number that you want to know the square root of. It then prompts the user to give an initial estimate (a reasonable estimate is deemed anything between 1 and the number itself). A while loop is then used to calculate the approximate square root (see formula above). The while loop will continue to iterate until the estimate is within 0.1 of the loop. Once this is achieved it exits the loop and prints the statement with the approximate square root.  
 

 
*References:*

https://docs.python.org/2/library/math.html 

Newton’s method https://tour.golang.org/flowcontrol/8 
 

__Question 8:__

A module called datetime() is imported as Python does not have its own built in.  The format of the date and time was as follows: 

Date: 

- %A = Weekday (full name) e.g. Monday 

- %B = Name of the Month(full name) e.g. March  

- %Y = Year e.g. 2019 

With regards the suffix associated with the date e.g. 10th, an if statement was applied in which a string with the variable month_date and the suffix was formed. If statement added the suffix to the month_date that was greater than and less than 21 or greater than 23 and less than 30. Else, uses the remainder function to assign a suffix to the month_date e.g. in the case of 21 when divided by 10 the remainder of 1 means that is 21st  


- %I = Hour (12 hour clock), e.g. 01 

- %M = Minute 00-59, e.g. 30 

- %p = AM/PM, e.g. AM 

- %I- to remove the zero before the number e.g. 05 -> 5 is fixed by uses the symbol # before the hour component in the time.  

%p – the way in which this is presented relates to the time zone of where the program has been run. Uppercase AM, PM (en_US) and lowercase am, pm (de_DE). In researching how to change the AM/PM that was outputted when %p was entered to the lowercase equivalent. I noticed there was a warning with respects the effect this may have, with a suggestion that it may alter the time to the timezone of which you are replacing it with. However, when I applied a replace function to the %p it did not alter the time at which the program was run. One article suggested by changing %p to %P this was solve the problem however this only appears to work on Linux systems that use glibc, however I do not have this.  

 
*References: *

https://docs.python.org/3.4/library/datetime.html?highlight=weekday 

https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

__Question 9: __
