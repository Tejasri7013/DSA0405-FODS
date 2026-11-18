import numpy as np
from scipy import stats

# Generate sample data
np.random.seed(42)
population = np.random.normal(loc=50, scale=10, size=1000)

# User inputs
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (90, 95, or 99): "))
precision = float(input("Enter desired precision (margin of error): "))

if n <= 1 or n > len(population):
    print("Invalid sample size!")
else:
    sample = np.random.choice(population, size=n, replace=False)

    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    confidence_level = confidence / 100

    margin = stats.t.ppf(
        (1 + confidence_level) / 2, n - 1
    ) * (std / np.sqrt(n))

    lower = mean - margin
    upper = mean + margin

    print("\nSample Mean:", round(mean, 2))
    print("Confidence Interval:", (round(lower, 2), round(upper, 2)))
    print("Margin of Error:", round(margin, 2))

    if margin <= precision:
        print("Desired precision achieved.")
    else:
        print("Desired precision not achieved.")