
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample data for 18 adults
data = {
    "Age": [23, 27, 31, 35, 39, 42, 45, 48, 52,
            55, 28, 33, 37, 41, 46, 50, 57, 60],
    "%Fat": [12.5, 15.2, 18.1, 20.4, 22.8, 25.1, 27.3, 29.5, 31.8,
             34.2, 16.4, 19.3, 21.7, 24.6, 26.8, 30.1, 33.5, 36.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean
print("Mean:")
print(df.mean())

# Calculate median
print("\nMedian:")
print(df.median())

# Calculate standard deviation
print("\nStandard Deviation:")
print(df.std())

# Boxplots
df.boxplot(column=["Age", "%Fat"])
plt.title("Boxplots of Age and Body Fat")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["%Fat"])
plt.xlabel("Age")
plt.ylabel("Body Fat Percentage")
plt.title("Age vs Body Fat")
plt.show()

# Q-Q plots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")

plt.subplot(1, 2, 2)
stats.probplot(df["%Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")

plt.tight_layout()
plt.show()

