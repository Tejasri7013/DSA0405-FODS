import pandas as pd

# Sample temperature dataset
data = {
    "Chennai": [30, 32, 31, 33, 34, 32, 31, 35, 33, 32],
    "Bangalore": [24, 25, 23, 26, 24, 25, 23, 24, 26, 25],
    "Mumbai": [28, 30, 29, 31, 32, 30, 29, 33, 31, 30],
    "Delhi": [20, 25, 22, 30, 35, 28, 24, 38, 32, 26]
}

df = pd.DataFrame(data)

print("Temperature Analysis")
print("--------------------")

# Calculate mean temperature
mean_temp = df.mean()
print("\nMean Temperature:")
print(mean_temp)

# Calculate standard deviation
std_temp = df.std()
print("\nStandard Deviation:")
print(std_temp)

# Calculate temperature range
temp_range = df.max() - df.min()
print("\nTemperature Range:")
print(temp_range)

# City with highest temperature range
highest_range_city = temp_range.idxmax()

# City with lowest standard deviation
consistent_city = std_temp.idxmin()

print("\nCity with Highest Temperature Range:",
      highest_range_city)

print("City with Most Consistent Temperature:",
      consistent_city)