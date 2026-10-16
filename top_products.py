import pandas as pd

# Create sample sales data

sales_data = pd.DataFrame({
'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard',
'Mouse', 'Laptop', 'Keyboard', 'Mouse'],
'quantity_sold': [10, 25, 15, 12, 30, 20, 18, 35],
'order_date': ['2026-10-01', '2026-10-02', '2026-10-03',
'2026-10-04', '2026-10-05', '2026-10-06',
'2026-10-07', '2026-10-08']
})

# Convert order_date to datetime

sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

# Find sales from the past month

last_month = sales_data[
sales_data['order_date'] >=
(pd.Timestamp.today() - pd.DateOffset(months=1))
]

# Calculate total quantity sold for each product

top_products = last_month.groupby('product_name')['quantity_sold'].sum()

# Display the top 5 products

print("Top 5 Best-Selling Products:")
print(top_products.sort_values(ascending=False).head(5))
