
import numpy as np
from scipy import stats

# Sample blood pressure reduction data
drug = np.array([
    12, 15, 10, 18, 14, 16, 13, 20, 11, 17,
    15, 19, 14, 16, 13, 18, 12, 21, 17, 15,
    14, 16, 19, 13, 18
])

placebo = np.array([
    4, 6, 3, 5, 7, 2, 8, 4, 5, 6,
    3, 7, 4, 5, 2, 6, 8, 3, 4, 5,
    7, 2, 6, 4, 5
])

# Function to calculate 95% confidence interval
def confidence_interval(data):
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    n = len(data)

    ci = stats.t.interval(
        0.95,
        df=n - 1,
        loc=mean,
        scale=std / np.sqrt(n)
    )

    return mean, ci

# Drug group
drug_mean, drug_ci = confidence_interval(drug)

# Placebo group
placebo_mean, placebo_ci = confidence_interval(placebo)

# Display results
print("Drug Group")
print("Mean Reduction:", round(drug_mean, 2))
print("95% Confidence Interval:",
      (round(drug_ci[0], 2), round(drug_ci[1], 2)))

print("\nPlacebo Group")
print("Mean Reduction:", round(placebo_mean, 2))
print("95% Confidence Interval:",
      (round(placebo_ci[0], 2), round(placebo_ci[1], 2)))
