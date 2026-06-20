# Exercise 6: Operations with variables

# In this exercise we will:
# 1. Ask the user for their name, age, and height (in meters)
# 2. Calculate the year the person was born
# 3. Calculate their Body Mass Index (BMI)
# 4. Use type() to verify the data type of each variable

print("=" * 64)

name = input("\nWhat's your name: ")
age = int(input("What's your age: "))
height = float(input("What's your height in meters: "))

print(f"\nMy name is {name}, I'm {age} yo and I'm {height}m tall.")

print("=" * 64)

current_year = int(input("\nWhat's the current year: "))
year_of_birth = current_year - age

print(f"\nI was born in {year_of_birth}.")

print("=" * 64)

weight = float(input("\nWhat's your weight in kg: "))

# Using Python's exponent operator (**) to square the height
BMI = weight / (height ** 2)

# We use ':.2f' inside the f-string to round the BMI to 2 decimal places!
print(f"\nMy BMI is {BMI:.2f}")

print("=" * 64)

# Step 4: Inspecting Data Types
print("\nEvery variable type: ")
print(type(name))          # Will show <class 'str'>
print(type(age))           # Will show <class 'int'>
print(type(height))        # Will show <class 'float'>
print(type(current_year))  # Will show <class 'int'>
print(type(year_of_birth)) # Will show <class 'int'>
print(type(weight))        # Will show <class 'float'>
print(type(BMI))           # Will show <class 'float'>