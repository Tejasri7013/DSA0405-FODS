
from collections import Counter
import re

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Split into words
words = text.split()

# Calculate word frequency
frequency = Counter(words)

# Display the result
print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
