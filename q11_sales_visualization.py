
import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [10000, 12000, 15000, 13000, 18000, 20000,
          22000, 21000, 19000, 25000, 27000, 30000]

# 1. Line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(months, sales)
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 3. Bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
