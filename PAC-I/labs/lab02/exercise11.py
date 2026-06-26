# Exercise 11: Business Logic and Percentages

# In this exercise, we will:
# 1. Ask the user for a product price, discount rate, and VAT rate
# 2. Calculate the monetary value of the discount
# 3. Apply the VAT to the newly discounted price, NOT the original price

print("=" * 64)

original_price = float(input("What's the original price of the product: "))
discount_percentage = float(input("What's the discount percentage (e.g., type 20 for 20%): "))
VAT_percentage = float(input("What's the VAT amount applied to the final price (e.g., type 15 for 15%): "))

# Step 1: Calculate the discount
discount = original_price * (discount_percentage / 100)
price_after_discount = original_price - discount

# Step 2: Calculate the VAT based on the discounted price
VAT_amount = price_after_discount * (VAT_percentage / 100)
final_price_VAT = price_after_discount + VAT_amount

# Used the ':.2f' trick to make the output look like real currency!
print(f"\nDiscount amount: ${discount:.2f}")
print(f"Price after discount: ${price_after_discount:.2f}")
print(f"VAT amount: ${VAT_amount:.2f}")
print(f"Final price with VAT: ${final_price_VAT:.2f}")

print("=" * 64)