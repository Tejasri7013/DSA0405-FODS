
from scipy.stats import chi2_contingency

# Website visitor data
visitors_A = 1000
conversions_A = 120

visitors_B = 1000
conversions_B = 150

# Calculate conversion rates
rate_A = conversions_A / visitors_A
rate_B = conversions_B / visitors_B

# Calculate non-conversions
non_A = visitors_A - conversions_A
non_B = visitors_B - conversions_B

# Create contingency table
data = [
    [conversions_A, non_A],
    [conversions_B, non_B]
]

# Perform Chi-square test
chi2, p_value, dof, expected = chi2_contingency(data)

# Display results
print("Conversion Rate A:", rate_A * 100, "%")
print("Conversion Rate B:", rate_B * 100, "%")
print("Chi-square value:", chi2)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Significant difference between Design A and Design B")
else:
    print("No significant difference between Design A and Design B")
