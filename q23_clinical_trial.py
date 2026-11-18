import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample clinical trial data
control = [2, 3, 2, 4, 3, 2, 5, 3, 4, 2]
treatment = [5, 6, 5, 7, 6, 5, 8, 7, 6, 5]

# Calculate mean
control_mean = np.mean(control)
treatment_mean = np.mean(treatment)

# Hypothesis testing using independent t-test
t_stat, p_value = stats.ttest_ind(
    treatment, control, equal_var=False
)

print("Clinical Trial Analysis")
print("--------------------")
print("Control Group Mean:", round(control_mean, 2))
print("Treatment Group Mean:", round(treatment_mean, 2))
print("T-statistic:", round(t_stat, 2))
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("\nThe treatment has a statistically significant effect.")
else:
    print("\nThe treatment has no statistically significant effect.")

# Visualization
plt.figure(figsize=(7, 5))
plt.boxplot([control, treatment],
            labels=["Control", "Treatment"])

plt.ylabel("Treatment Response")
plt.title("Clinical Trial Comparison")
plt.grid(axis="y")
plt.show()

# P-value visualization
plt.figure(figsize=(6, 4))
plt.bar(["P-value", "Significance Level"],
        [p_value, 0.05])

plt.ylabel("Value")
plt.title("P-value vs Significance Level")
plt.show()