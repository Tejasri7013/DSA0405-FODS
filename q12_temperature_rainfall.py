
import matplotlib.pyplot as plt

# Monthly data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [22, 24, 28, 32, 35, 38, 36, 34, 32, 29, 26, 23]

rainfall = [20, 15, 25, 40, 60, 120, 200, 180, 150, 100, 50, 30]

# 1. Line plot for temperature
plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2. Scatter plot for rainfall
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
