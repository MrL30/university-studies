# Exercise 4: The input() function

# In this exercise, we will ask the user for their name and greet them
# The input() function prints a message to the terminal and freezes the program
# It waits until the user types something and presses the 'Enter' key

# We take whatever the user types and store it in the variable 'name'
name = input("\nWhat's your name: ")

# Note: The input() function ALWAYS gives us back a string (text)
# Now, we inject their name into our greeting!
print(f"Hello, {name}!\n")