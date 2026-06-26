# Exercise 7: Swapping Variable Values

# In this exercise, we will swap the values of two variables
# Imagine 'x' is a glass of milk and 'y' is a glass of juice
# To swap them, we need a third empty glass called 'temp'

print("=" * 64)

x = 10
y = 5

print(f"Before the change: x = {x} and y = {y}")

temp = x  # Pour the milk (10) into the empty glass
x = y     # Pour the juice (5) into the 'x' glass
y = temp  # Pour the milk (10) from the 'temp' glass into the 'y' glass

print(f"After the change: x = {x} and y = {y}")

print("=" * 64)
