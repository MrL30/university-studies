# Exercise 9: Data Types and Type Conversion

# In this exercise, we will:
# 1. Ask the user for data
# 2. Convert that data into specific types: integer, float, and string
# 3. Prove the conversion worked using the type() function

print("=" * 64)

name = input("What's your name: ")

# We use int() to convert the string into a whole number
age = int(input("What's your age: "))

# We use float() to convert the string into a decimal number
price = float(input("What's the price of your product: "))

# Now we print the values and use type() to prove what they are under the hood
print(f"\nName entered: {name} (type: {type(name)})")
print(f"Age entered: {age} (type: {type(age)})")
print(f"Price entered: {price} (type: {type(price)})")

print("=" * 64)