# Exercise 1: Divisibility and the Modulo Operator

# In this exercise, we will:
# 1. Ask the user for two integers
# 2. Make sure the second number isn't zero (to prevent a crash)
# 3. Use the modulo operator (%) to check if they are divisible

print("=" * 64)

num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))

if num_2 == 0:
    print("\nError: You cannot divide by zero! Please try again with a different number.")
    
# If num_2 is safe, we move on to your exact modulo logic
elif num_1 % num_2 == 0:
    print(f"\n{num_1} is divisible by {num_2}")
    
else:
    print(f"\n{num_1} is not divisible by {num_2}\n")

print("=" * 64)

