# Exercise 8: Control Flow and Modules

import datetime

# In this exercise, we will:
# 1. Ask the user for their current age and ideal retirement age.
# 2. Check IF they are already old enough to retire.
# 3. If not, calculate how many years are left and what year that will be.

print("=" * 64)

current_age = int(input("What's your current age: "))
retire_age = int(input("What's your ideal retirement age: "))

# The IF Statement: Python checks if this condition is True
if current_age >= retire_age:
    print("\nYou can officially retire!!")
    
# The ELSE Statement: If the condition above was False, Python runs this code instead
else:
    years_to_retire = retire_age - current_age
    
    # We use the 'datetime' module to get the exact current year dynamically!
    current_year = datetime.date.today().year
    retire_year = current_year + years_to_retire
    
    print(f"\nYou have {years_to_retire} years left until you can retire.")
    print(f"It will be the year {retire_year} when you retire.")

print("=" * 64)