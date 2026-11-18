from sklearn.tree import DecisionTreeRegressor

# Sample car dataset
# Features: Mileage, Age, Engine Capacity (CC)
X = [
    [15000, 1, 1200],
    [25000, 2, 1200],
    [35000, 3, 1500],
    [45000, 4, 1500],
    [60000, 5, 1800],
    [75000, 6, 1800],
    [90000, 7, 2000],
    [110000, 8, 2000],
    [20000, 1, 1000],
    [50000, 4, 1200],
    [80000, 6, 1500],
    [100000, 8, 1800]
]

# Car prices in rupees
y = [
    900000, 800000, 700000, 600000,
    500000, 400000, 300000, 200000,
    950000, 550000, 350000, 250000
]

feature_names = ["Mileage", "Age", "Engine Capacity"]

# Create CART regression model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Input new car details
mileage = float(input("Enter car mileage (km): "))
age = int(input("Enter car age (years): "))
engine = int(input("Enter engine capacity (CC): "))

car = [[mileage, age, engine]]

# Predict car price
predicted_price = model.predict(car)

print("\nCar Price Prediction")
print("------------------")
print("Predicted Price: Rs.", round(predicted_price[0], 2))

# Display decision path
decision_path = model.decision_path(car)
tree = model.tree_

print("\nDecision Path:")
for node in decision_path.indices:
    if tree.feature[node] != -2:
        feature = feature_names[tree.feature[node]]
        threshold = tree.threshold[node]

        if car[0][tree.feature[node]] <= threshold:
            print(feature, "<=", round(threshold, 2))
        else:
            print(feature, ">", round(threshold, 2))