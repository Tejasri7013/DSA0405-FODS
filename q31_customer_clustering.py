import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample customer dataset
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Spending": [1000, 1200, 1500, 2000, 5000, 5500, 6000, 8000, 3000, 3500],
    "Purchases": [5, 6, 8, 10, 20, 22, 25, 30, 12, 15]
}

df = pd.DataFrame(data)

# Select features
X = df[["Spending", "Purchases"]]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Segmentation Results:")
print(df)

# Visualize clusters
plt.scatter(df["Spending"], df["Purchases"],
            c=df["Cluster"], cmap="viridis")

plt.xlabel("Customer Spending")
plt.ylabel("Number of Purchases")
plt.title("Customer Segmentation using K-Means")
plt.colorbar(label="Cluster")
plt.show()