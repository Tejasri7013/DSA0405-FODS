import pandas as pd

# Create sample order data
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': ['2026-01-10', '2026-01-12', '2026-01-15', '2026-01-18', '2026-01-20'],
    'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse'],
    'order_quantity': [2, 3, 1, 2, 5]
})

# 1. Total orders by each customer
print("Total orders by each customer:")
print(order_data.groupby('customer_id').size())

# 2. Average order quantity for each product
print("\nAverage order quantity for each product:")
print(order_data.groupby('product_name')['order_quantity'].mean())

# 3. Earliest and latest order dates
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

print("\nEarliest order date:", order_data['order_date'].min())
print("Latest order date:", order_data['order_date'].max())