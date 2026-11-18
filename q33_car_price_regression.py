import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample car dataset
data = {
    "Engine_Size": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500, 4000],
    "Horsepower": [70, 85, 100, 120, 150, 170, 190, 220, 260, 300],
    "Mileage": [22, 20, 18, 16, 14, 13, 12, 10, 9, 8],
    "Price": [500000, 600000, 800000, 1000000, 1500000,
              1800000, 2200000, 2800000, 3500000, 4500000]
}

df = pd.DataFrame(data)

# Select features and target
X = df[["Engine_Size", "Horsepower", "Mileage"]]
y = df["Price"]

# Create and train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Input car details
engine = float(input("Enter engine size (CC): "))
hp = float(input("Enter horsepower: "))
mileage = float(input("Enter mileage (km/l): "))

# Predict price
car = [[engine, hp, mileage]]
predicted_price = model.predict(car)

print("\nPredicted Car Price:", round(predicted_price[0], 2))

# Evaluate model
y_pred = model.predict(X)

print("\nModel Evaluation")
print("MSE:", round(mean_squared_error(y, y_pred), 2))
print("R2 Score:", round(r2_score(y, y_pred), 4))

# Feature importance using coefficients
print("\nFeature Influence:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", round(coefficient, 2))

# Actual vs Predicted graph
plt.scatter(y, y_pred)
plt.xlabel("Actual Car Prices")
plt.ylabel("Predicted Car Prices")
plt.title("Actual vs Predicted Car Prices")
plt.show()