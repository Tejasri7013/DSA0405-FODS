
import pandas as pd

# Create order data
order_data = pd.DataFrame({
    'Customer_ID': [101, 102, 101, 103, 102, 101, 103],
    'Order_Date': ['2025-01-10', '2025-01-12', '2025-01-15',
                   '2025-01-18', '2025-01-20', '2025-01-22',
                   '2025-01-25'],
    'Product_Name': ['Laptop', 'Phone', 'Laptop', 'Tablet',
                     'Phone', 'Tablet', 'Laptop'],
    'Order_Quantity': [1, 2, 1, 3, 1, 2, 2]
})

# Convert Order_Date into datetime format
order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

# 1. Total orders made by each customer
orders_per_customer = order_data.groupby('Customer_ID').size()

# 2. Average order quantity for each product
average_quantity = order_data.groupby('Product_Name')['Order_Quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

# Display results
print("Order Data:")
print(order_data)

print("\nTotal orders made by each customer:")
print(orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_quantity)

print("\nEarliest order date:", earliest_date)
print("Latest order date:", latest_date)
