# Exercise 12: Trigonometry and the Math Module

import math

# In this exercise, we will:
# 1. Ask the user for an angle in degrees
# 2. Convert those degrees to radians (which Python requires for trig)
# 3. Calculate the sine and cosine of the angle
# 4. Prove the Pythagorean identity: sin^2(x) + cos^2(x) = 1

print("=" * 64)

x = int(input("\nAngle value (in degrees): "))

# Computers calculate trig using radians, so we must convert first!
y = math.radians(x)

# Calculate sine and cosine
sine = math.sin(y)
cosine = math.cos(y)

print(f"\nSine({x}): {sine:.4f}")
print(f"Cosine({x}): {cosine:.4f}")

# Proving the Pythagorean identity! 
# We round it to handle floating-point precision quirks
pythagorean_identity = (sine ** 2) + (cosine ** 2)
print(f"The sum of the squares of sin({x}) and cos({x}) = {pythagorean_identity:.2f}\n")

print("=" * 64)