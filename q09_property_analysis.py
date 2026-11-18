
import pandas as pd

# Create property data
property_data = pd.DataFrame({
    'Property_ID': [101, 102, 103, 104, 105, 106],
    'Location': ['Chennai', 'Bangalore', 'Chennai',
                'Hyderabad', 'Bangalore', 'Chennai'],
    'Bedrooms': [3, 5, 4, 6, 2, 5],
    'Area_sqft': [1500, 2500, 1800, 3000, 1200, 2200],
    'Listing_Price': [5000000, 8000000, 6500000,
                      9000000, 4000000, 7500000]
})

# 1. Average listing price in each location
average_price = property_data.groupby('Location')['Listing_Price'].mean()

# 2. Number of properties with more than 4 bedrooms
count_properties = (property_data['Bedrooms'] > 4).sum()

# 3. Property with the largest area
largest_property = property_data.loc[property_data['Area_sqft'].idxmax()]

# Display results
print("Property Data:")
print(property_data)

print("\nAverage listing price in each location:")
print(average_price)

print("\nNumber of properties with more than 4 bedrooms:",
      count_properties)

print("\nProperty with the largest area:")
print(largest_property)
