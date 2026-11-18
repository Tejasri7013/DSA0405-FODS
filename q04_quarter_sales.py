
import numpy as np

# Sales data for four quarters
sales_data = np.array([25000, 30000, 35000, 45000])

# Calculate total sales
total_sales = np.sum(sales_data)

# Calculate percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) /
                       sales_data[0]) * 100

# Display results
print("Quarterly Sales:", sales_data)
print("Total Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4:",
      percentage_increase, "%")
