# Exercise 2: About the print function

# The print function is used to display text and information on the screen
# We use quotation marks to tell Python: "Print exactly these words"
print("Hello, World!") 

height = 1.81

# If we don't use quotes, Python knows it should look for a variable or do math
print(height) 
print(1 + height)

# We can print multiple items at once by separating them with commas
# Notice how Python automatically adds a space between the items for us!
print("My height is", height, "meters")

# 'F-strings' (Format strings) are the best way to format text
# The 'f' at the start tells Python to look for curly braces {} and swap in our variables
print(f"My height is {height} meters")

# F-strings are highly recommended because they are the most readable!
