from sklearn.linear_model import LogisticRegression

# Sample customer dataset
# Features: Usage minutes, Contract duration (months)
X = [
    [500, 24],
    [600, 36],
    [200, 6],
    [150, 3],
    [700, 24],
    [100, 2],
    [400, 12],
    [250, 6],
    [800, 36],
    [180, 3]
]

# Churn labels: 0 = No churn, 1 = Churn
y = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]

# Create Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# Input new customer details
usage = float(input("Enter monthly usage minutes: "))
contract = int(input("Enter contract duration (months): "))

customer = [[usage, contract]]

# Predict churn
prediction = model.predict(customer)

print("\nCustomer Churn Prediction:")

if prediction[0] == 1:
    print("Customer is likely to churn.")
else:
    print("Customer is not likely to churn.")