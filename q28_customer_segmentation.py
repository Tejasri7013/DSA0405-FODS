from sklearn.cluster import KMeans

# Sample customer data
# Features: Annual spending, Number of purchases
X = [
    [1000, 5],
    [1200, 6],
    [1500, 8],
    [2000, 10],
    [5000, 20],
    [5500, 22],
    [6000, 25],
    [8000, 30],
    [3000, 12],
    [3500, 15]
]

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

# Input new customer data
spending = float(input("Enter annual spending: "))
purchases = int(input("Enter number of purchases: "))

customer = [[spending, purchases]]

# Predict cluster
cluster = model.predict(customer)

print("\nCustomer Segmentation Result")
print("Customer belongs to Cluster:", cluster[0])