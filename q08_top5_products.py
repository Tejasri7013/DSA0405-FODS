
import pandas as pd

# Create sales data
sales_data = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop',
                'Headphones', 'Phone', 'Tablet', 'Laptop',
                'Smartwatch', 'Headphones'],
    'Quantity_Sold': [10, 25, 15, 20, 30, 35, 10, 15, 18, 12]
})

# Calculate total sales quantity for each product
product_sales = sales_data.groupby('Product')['Quantity_Sold'].sum()

# Find top 5 best-selling products
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Display results
print("Total quantity sold for each product:")
print(product_sales)

print("\nTop 5 best-selling products:")
print(top_5_products)
