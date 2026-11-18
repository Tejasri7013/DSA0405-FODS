import pandas as pd
import matplotlib.pyplot as plt

# Sample student data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Scores": [35, 40, 45, 50, 55, 65, 70, 75, 85, 95]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["Study_Hours"].corr(df["Exam_Scores"])

print("Study Time and Exam Score Analysis")
print("---------------------------------")
print("Correlation Coefficient:", round(correlation, 2))

if correlation > 0:
    print("Positive correlation")
elif correlation < 0:
    print("Negative correlation")
else:
    print("No correlation")

# Scatter plot
plt.scatter(df["Study_Hours"], df["Exam_Scores"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")
plt.grid()
plt.show()

# Line plot
plt.plot(df["Study_Hours"], df["Exam_Scores"], marker="o")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Time and Exam Score Trend")
plt.grid()
plt.show()

# Histogram of exam scores
plt.hist(df["Exam_Scores"], bins=5)
plt.xlabel("Exam Scores")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.grid()
plt.show()