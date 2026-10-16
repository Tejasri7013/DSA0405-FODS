import matplotlib.pyplot as plt

# Monthly sales data

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 15000, 12000, 18000, 20000, 25000]

# 1. Line plot

plt.plot(months, sales, marker='o')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# 2. Bar plot

plt.bar(months, sales)
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
