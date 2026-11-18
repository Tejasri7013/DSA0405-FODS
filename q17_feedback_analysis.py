
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

# Dataset included directly in the code
data = {
    "feedback": [
        "The product is very good",
        "The product quality is excellent",
        "Good quality and good service",
        "The service is fast and excellent",
        "Product quality is good",
        "Very good customer service"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Stop words
stop_words = {
    "the", "is", "and", "a", "an", "in", "of", "to",
    "for", "with", "on", "this", "that", "it", "very"
}

all_words = []

# Preprocessing
for feedback in df["feedback"]:
    feedback = feedback.lower()
    feedback = re.sub(r'[^\w\s]', '', feedback)
    words = feedback.split()
    words = [word for word in words if word not in stop_words]
    all_words.extend(words)

# Word frequency
frequency = Counter(all_words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)

# User input
n = int(input("\nEnter the number of top words: "))

# Top N words
top_words = frequency.most_common(n)

print("\nTop", n, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Plot graph
words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top N Words in Customer Feedback")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
