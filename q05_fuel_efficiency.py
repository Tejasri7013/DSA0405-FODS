
import numpy as np

# Fuel efficiency of car models (in miles per gallon)
fuel_efficiency = np.array([25, 30, 35, 40, 45])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement between two car models
car1 = fuel_efficiency[0]
car2 = fuel_efficiency[4]

percentage_improvement = ((car2 - car1) / car1) * 100

# Display results
print("Fuel Efficiency:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Car 1 Fuel Efficiency:", car1, "MPG")
print("Car 2 Fuel Efficiency:", car2, "MPG")
print("Percentage Improvement:", percentage_improvement, "%")
