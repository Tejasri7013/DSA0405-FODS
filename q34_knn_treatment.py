import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sample patient dataset
data = {
    "Age": [25, 30, 45, 50, 35, 60, 28, 42, 55, 32, 48, 65, 23, 38, 52, 29, 57, 40, 34, 62],
    "BP": [110, 120, 140, 150, 130, 160, 115, 135, 155, 125, 145, 165, 108, 128, 148, 118, 158, 138, 122, 162],
    "Cholesterol": [180, 190, 240, 250, 210, 270, 185, 220, 260, 200, 245, 280, 175, 205, 255, 188, 265, 230, 195, 275],
    "Outcome": ["Good", "Good", "Bad", "Bad", "Good", "Bad", "Good", "Good", "Bad", "Good", "Bad", "Bad", "Good", "Good", "Bad", "Good", "Bad", "Good", "Good", "Bad"]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Age", "BP", "Cholesterol"]]
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Display predictions
print("Test Set Predictions")
print("------------------")
for actual, predicted in zip(y_test, y_pred):
    print("Actual:", actual, "| Predicted:", predicted)

# Evaluation metrics
print("\nModel Evaluation")
print("--------------")
print("Accuracy :", round(accuracy_score(y_test, y_pred), 2))
print("Precision:", round(precision_score(y_test, y_pred, pos_label="Good"), 2))
print("Recall   :", round(recall_score(y_test, y_pred, pos_label="Good"), 2))
print("F1 Score :", round(f1_score(y_test, y_pred, pos_label="Good"), 2))

# Predict a new patient
age = int(input("\nEnter patient age: "))
bp = int(input("Enter blood pressure: "))
cholesterol = int(input("Enter cholesterol level: "))

new_patient = scaler.transform([[age, bp, cholesterol]])
prediction = model.predict(new_patient)

print("Predicted Treatment Outcome:", prediction[0])