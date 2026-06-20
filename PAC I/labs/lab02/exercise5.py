# Exercise 5: Creating the first program

# In this exercise, we will:
# 1. Ask for the user's name and greet them.
# 2. Ask for their age and calculate how old they will be in 10 years.
# 3. Ask for their city and count the number of characters in its name.

print(64 * "=")

# Step 1: Strings
name = input("What's your name: ")
print(f"Hello, {name}!")

# Step 2: Type Casting (Converting Strings to Integers)
# input() gives us text. We wrap it in int() to turn that text into a math-ready number.
age = int(input("How old are you: "))
print(f"In ten years you'll be {age + 10}")

# Step 3: The len() function
city = input("What's the name of the city you live in: ")
# len() counts the number of characters (including spaces!) in a string.
print(f"The city {city} has {len(city)} characters in its name")

print(64 * "=")

# Step 4: Putting it all together
# We can combine variables, math, and functions all inside one f-string!
print(f"\nHello {name}! Your name has {len(name)} characters, that's so cool! In ten years you will be {age + 10} years old, what do you see yourself doing in that time? You live in {city}, such a beautiful city, it has {len(city)} characters in its name.\n")

print(64 * "=")