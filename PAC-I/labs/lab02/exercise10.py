# Exercise 10: Geometry and the Math Module

# In this exercise, we will:
# 1. Import the value of 'pi' from Python's built-in math module
# 2. Calculate the area and perimeter of a circle
# 3. Calculate the area and perimeter of a square

from math import pi

print("=" * 64)

# --- Circle Calculations ---
circle_radius = float(input("\nWhat's the circle radius: "))
circle_area = pi * (circle_radius ** 2)
circle_perimeter = 2 * pi * circle_radius

# Because pi is so long, we use ':.2f' to round the results to 2 decimal places
print(f"\nCircle Area: {circle_area:.2f}")
print(f"Circle Perimeter: {circle_perimeter:.2f}\n")

print("=" * 64)

# --- Square Calculations ---
square_side = float(input("\nWhat's the length of the square side: "))
square_area = square_side ** 2
square_perimeter = square_side * 4

print(f"\nSquare Area: {square_area:.2f}")
print(f"Square Perimeter: {square_perimeter:.2f}\n")

print("=" * 64)