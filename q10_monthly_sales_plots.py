
import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [12000, 15000, 18000, 16000, 20000, 22000,
          25000, 23000, 21000, 26000, 28000, 30000]

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
