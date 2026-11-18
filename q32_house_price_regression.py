import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample house dataset
data = {
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500],
    "Price": [200000, 250000, 300000, 350000, 400000,
              440000, 500000, 560000, 600000, 700000]
}

df = pd.DataFrame(data)

# Bivariate analysis
print("Correlation:", df["Area"].corr(df["Price"]))

# Scatter plot
plt.scatter(df["Area"], df["Price"])
plt.xlabel("House Area (sq.ft)")
plt.ylabel("House Price")
plt.title("Bivariate Analysis of Area and Price")
plt.show()

# Linear Regression
X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# Prediction
area = float(input("Enter house area (sq.ft): "))
predicted_price = model.predict([[area]])

print("\nPredicted House Price:", round(predicted_price[0], 2))

# Model evaluation
y_pred = model.predict(X)

print("Mean Squared Error:", round(mean_squared_error(y, y_pred), 2))
print("R2 Score:", round(r2_score(y, y_pred), 4))

# Regression line
plt.scatter(X, y, label="Actual Prices")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("House Area (sq.ft)")
plt.ylabel("House Price")
plt.title("Linear Regression - House Price Prediction")
plt.legend()
plt.show()