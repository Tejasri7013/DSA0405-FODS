import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample retail customer dataset
data = {
    "CustomerID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Spending": [500, 700, 1000, 1500, 4000, 4500, 5000, 7000, 2500, 3000],
    "Visits": [2, 3, 4, 5, 15, 18, 20, 25, 8, 10]
}

df = pd.DataFrame(data)

# Select features
X = df[["Spending", "Visits"]]

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X_scaled)

# Display results
print("Retail Customer Segmentation")
print("-------------------------")
print(df)

# Visualization
plt.scatter(df["Spending"], df["Visits"],
            c=df["Cluster"], cmap="viridis")

plt.xlabel("Customer Spending")
plt.ylabel("Number of Visits")
plt.title("Retail Customer Segmentation")
plt.colorbar(label="Cluster")
plt.show()