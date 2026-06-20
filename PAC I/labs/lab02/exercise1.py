# Exercise 1: Getting started with Python

# The '#' symbol creates a comment. Python completely ignores these lines, 
# so we use them to leave notes for ourselves and other programmers!

# 1. Python as a Calculator
# Python follows standard math rules to solve expressions
print((72.7 * 1.81) - 58) 

# 2. Creating Variables
# Think of a variable as a sticky note. Here, we write "height" on a sticky note 
# and attach it to the number 1.81
height = 1.81

# Now, instead of typing the number, we can just print the variable
print(height)

# 3. Using Variables in Math
# Python will look at the variable 'height', swap in the number 1.81, 
# and then solve the math
print((72.7 * height) - 58) 

# We can even save the final result of that math inside a brand-new variable
weight = (72.7 * height) - 58

# 4. The Top-to-Bottom Rule
# Python reads code from line 1 downwards. If we try to use a variable 
# before we define it, Python will panic and give us a "NameError"
# (Try removing the '#' from the line below to see the error!)
# print(sky)