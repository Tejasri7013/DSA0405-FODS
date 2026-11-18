
# Item prices and quantities
prices = [100, 200, 150, 50]
quantities = [2, 1, 3, 2]

# Discount and tax rates
discount_rate = 10  # 10%
tax_rate = 5       # 5%

# Calculate total price before discount
total = 0

for i in range(len(prices)):
    total = total + (prices[i] * quantities[i])

# Calculate discount
discount = total * discount_rate / 100

# Price after discount
discounted_price = total - discount

# Calculate tax
tax = discounted_price * tax_rate / 100

# Final cost
final_cost = discounted_price + tax

# Display results
print("Total price before discount:", total)
print("Discount amount:", discount)
print("Price after discount:", discounted_price)
print("Tax amount:", tax)
print("Final cost:", final_cost)
