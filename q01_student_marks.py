
import numpy as np

# Marks of 4 students in 4 subjects
# Columns: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 87, 85, 80],
    [76, 95, 89, 84],
    [88, 82, 92, 90]
])

# Calculate average marks of each subject
subject_averages = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

# Display average marks
print("Average marks of each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])

# Find the subject with the highest average
highest_index = np.argmax(subject_averages)

print("\nSubject with highest average marks:",
      subjects[highest_index])
print("Highest average:",
      subject_averages[highest_index])
