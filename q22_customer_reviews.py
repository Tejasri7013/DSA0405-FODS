import pandas as pd
import numpy as np
from scipy import stats

# Sample customer ratings
ratings = [5, 4, 4, 5, 3, 5, 4, 4, 5, 3,
           4, 5, 4, 2, 5, 4, 3, 5, 4, 5]

df = pd.DataFrame({"Rating": ratings})

# Calculate statistics
mean_rating = df["Rating"].mean()
std = df["Rating"].std()
n = len(df)

# 95% confidence interval
confidence = 0.95
t_value = stats.t.ppf((1 + confidence) / 2, n - 1)
margin = t_value * (std / np.sqrt(n))

lower = mean_rating - margin
upper = mean_rating + margin

print("Customer Review Analysis")
print("---------------------")
print("Number of Reviews:", n)
print("Average Rating:", round(mean_rating, 2))
print("Standard Deviation:", round(std, 2))
print("95% Confidence Interval:",
      (round(lower, 2), round(upper, 2)))

if mean_rating >= 4:
    print("Customer Satisfaction: High")
elif mean_rating >= 3:
    print("Customer Satisfaction: Moderate")
else:
    print("Customer Satisfaction: Low")