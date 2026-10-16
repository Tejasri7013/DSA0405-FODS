import pandas as pd

# Create sample property data

property_data = pd.DataFrame({
'property_id': [101, 102, 103, 104, 105],
'location': ['Chennai', 'Bangalore', 'Chennai', 'Hyderabad', 'Bangalore'],
'bedrooms': [3, 5, 4, 6, 2],
'area_sqft': [1200, 2000, 1500, 2500, 1000],
'listing_price': [5000000, 8000000, 6000000, 9000000, 4000000]
})

# 1. Average listing price in each location

print("Average Listing Price by Location:")
print(property_data.groupby('location')['listing_price'].mean())

# 2. Number of properties with more than four bedrooms

print("\nProperties with more than four bedrooms:")
print((property_data['bedrooms'] > 4).sum())

# 3. Property with the largest area

print("\nProperty with the Largest Area:")
print(property_data.loc[property_data['area_sqft'].idxmax()])
