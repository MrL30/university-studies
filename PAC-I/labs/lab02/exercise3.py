# Exercise 3: Debbuging some code

# Original code with errors:

"""
print(Hello world!")
print("The result of 10 + 2 is: " + 10 + 2)
print('This string is missing an ending quote)
print("Mixing" 'different' "types of quotes in one statement")
print('Backslashes can be tricky! Watch out for \n newline')
print("This message will end with a period", ".")
print("What's wrong with this statement?')
print("Adding numbers and strings doesn't work: " + 10)
"""

# Fixed code:

# 1. Missing Quotes
print("Hello world!") 
# FIX: Added the missing quotation mark at the beginning of the string

# 2. TypeErrors (Combining Strings and Math)
print("The result of 10 + 2 is: ", 10 + 2) 
# FIX: Replaced the '+' with a comma. We cannot use '+' to combine strings with integers (whole numbers)

# 3. Mismatched Quotes
print('This string is missing an ending quote') 
# FIX: Added the missing single quote at the end of the string

# 4. Escape Characters (Quotes)
print("Mixing\" \'different\' \"types of quotes in one statement") 
# FIX: To print quotation marks inside a string without confusing Python, we use the escape character (\)

# 5. Escape Characters (Newlines)
print('Backslashes can be tricky! Watch out for \\n newline') 
# FIX: We added a second backslash to "escape" the first one, stopping it from creating a new line

# 6. Unwanted Spaces
print("This message will end with a period" + ".") 
# FIX: The comma adds a space. By using the '+' sign with two strings, we glue them together with no spaces!

# 7. Inconsistent Quotes
print("What's wrong with this statement?") 
# FIX: A string must start and end with the exact same type of quote

# 8. TypeErrors (Combining Strings and Numbers)
print("Adding numbers and strings doesn't work: ", 10) 
# FIX: Just like line 2, we must use a comma to separate a string and an integer