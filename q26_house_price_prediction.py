from sklearn.linear_model import LinearRegression

# Sample house dataset
# Features: Area, Bedrooms, Bathrooms
X = [
    [1000, 2, 1],
    [1200, 2, 2],
    [1500, 3, 2],
    [1800, 3, 2],
    [2000, 4, 3],
    [2500, 4, 3],
    [3000, 5, 3],
    [3500, 5, 4]
]

# House prices
y = [200000, 250000, 300000, 350000,
     400000, 500000, 600000, 700000]

# Create Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Input new house details
area = float(input("Enter house area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))

# Predict house price
house = [[area, bedrooms, bathrooms]]
predicted_price = model.predict(house)

print("\nPredicted House Price:",
      round(predicted_price[0], 2))