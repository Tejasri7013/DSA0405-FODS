from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Input flower measurements
sepal_length = float(input("Enter sepal length (cm): "))
sepal_width = float(input("Enter sepal width (cm): "))
petal_length = float(input("Enter petal length (cm): "))
petal_width = float(input("Enter petal width (cm): "))

# Predict species
flower = [[sepal_length, sepal_width,
           petal_length, petal_width]]

prediction = model.predict(flower)

print("\nPredicted Iris Species:",
      iris.target_names[prediction[0]])