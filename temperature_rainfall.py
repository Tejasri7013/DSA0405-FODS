import matplotlib.pyplot as plt

# Monthly data

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [22, 24, 28, 32, 35, 34, 31, 30, 29, 27, 24, 22]
rainfall = [20, 15, 25, 40, 60, 150, 200, 180, 160, 100, 50, 25]

# 1. Line plot of monthly temperature

plt.figure()
plt.plot(months, temperature, marker='o')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()

# 2. Scatter plot of monthly rainfall

plt.figure()
plt.scatter(months, rainfall)
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.show()
