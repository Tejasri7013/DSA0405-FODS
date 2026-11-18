
import pandas as pd
import matplotlib.pyplot as plt

# Sample customer data
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [22, 25, 22, 30, 25, 35, 30, 22, 40, 25]
}

df = pd.DataFrame(data)

# Calculate age frequency
frequency = df["Age"].value_counts().sort_index()

# Display frequency distribution
print("Frequency Distribution of Customer Ages:")
print(frequency)

# Plot the frequency distribution
frequency.plot(kind="bar", color="skyblue")

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Customer Age Frequency Distribution")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
