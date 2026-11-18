from sklearn.neighbors import KNeighborsClassifier

# Sample patient dataset
# Features: Fever, Cough, Fatigue
X = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Labels: 0 = No condition, 1 = Condition
y = [0, 0, 1, 0, 1, 0, 1, 1]

# Create KNN model
k = int(input("Enter the value of k: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Input new patient symptoms
fever = int(input("Fever (0=No, 1=Yes): "))
cough = int(input("Cough (0=No, 1=Yes): "))
fatigue = int(input("Fatigue (0=No, 1=Yes): "))

patient = [[fever, cough, fatigue]]

# Prediction
prediction = model.predict(patient)

print("\nPatient Prediction:")

if prediction[0] == 1:
    print("Patient has the medical condition.")
else:
    print("Patient does not have the medical condition.")