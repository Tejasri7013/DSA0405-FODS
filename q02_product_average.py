
import numpy as np

# Sales prices of 3 products
# Each row represents a product
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [400, 450, 500]
])

# Calculate average price of all products
average_price = np.mean(sales_data)

# Display the result
print("Sales Data:")
print(sales_data)

print("\nAverage price of all products:", average_price)
