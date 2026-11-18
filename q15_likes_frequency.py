
import pandas as pd
import matplotlib.pyplot as plt

# Sample post data
data = {
    "Post_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Likes": [100, 150, 100, 200, 150, 250, 100, 300, 200, 150]
}

df = pd.DataFrame(data)

# Calculate frequency of likes
frequency = df["Likes"].value_counts().sort_index()

# Display frequency distribution
print("Frequency Distribution of Likes:")
print(frequency)

# Plot frequency distribution
frequency.plot(kind="bar", color="orange")

plt.xlabel("Number of Likes")
plt.ylabel("Frequency")
plt.title("Likes Frequency Distribution")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
