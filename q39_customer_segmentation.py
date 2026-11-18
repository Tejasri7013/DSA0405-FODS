import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample customer transaction dataset
data = {
    "Customer_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],
    "Amount_Spent": [
        500, 700, 600, 800, 900,
        2000, 2200, 2500, 2300, 2100,
        5000, 5500, 6000, 5800, 5200
    ],
    "Items_Purchased": [
        2, 3, 2, 4, 3,
        6, 7, 8, 7, 6,
        12, 13, 15, 14, 12
    ]
}

df = pd.DataFrame(data)

print("Customer Transaction Data:")
print(df)

# Select features for clustering
X = df[["Amount_Spent", "Items_Purchased"]]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Display customer clusters
print("\nCustomer Segmentation Results:")
print(df)

# Display number of customers in each cluster
print("\nCustomers in Each Cluster:")
print(df["Cluster"].value_counts().sort_index())

# Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Amount_Spent"],
    df["Items_Purchased"],
    c=df["Cluster"],
    cmap="viridis",
    s=100
)

plt.xlabel("Amount Spent")
plt.ylabel("Number of Items Purchased")
plt.title("Customer Segmentation Using K-Means")
plt.colorbar(label="Cluster")
plt.grid(True)
plt.show()