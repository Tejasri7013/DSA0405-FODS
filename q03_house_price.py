
import numpy as np

# House data
# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 1800, 250000],
    [6, 3000, 450000],
    [5, 2200, 320000],
    [2, 1200, 150000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Extract sale prices
sale_prices = selected_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

# Display results
print("Houses with more than 4 bedrooms:")
print(selected_houses)

print("\nSale prices:", sale_prices)
print("Average sale price:", average_price)
