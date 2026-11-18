import pandas as pd
import matplotlib.pyplot as plt

# Create soccer player dataset
data = {
    "Name": [
        "Messi", "Ronaldo", "Neymar", "Mbappe",
        "Haaland", "Salah", "Kane", "De Bruyne",
        "Modric", "Benzema", "Vinicius", "Son"
    ],

    "Age": [
        38, 41, 34, 27, 26, 34,
        33, 35, 41, 38, 26, 34
    ],

    "Position": [
        "Forward", "Forward", "Forward", "Forward",
        "Forward", "Forward", "Forward", "Midfielder",
        "Midfielder", "Forward", "Forward", "Forward"
    ],

    "Goals": [
        850, 950, 450, 350, 300, 350,
        320, 150, 80, 450, 120, 250
    ],

    "Weekly_Salary": [
        1000000, 900000, 700000, 800000,
        600000, 400000, 500000, 450000,
        300000, 550000, 350000, 400000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset into CSV file
df.to_csv("soccer_players.csv", index=False)

print("Dataset created and saved successfully!")

# Read CSV file
df = pd.read_csv("soccer_players.csv")

print("\nSoccer Player Dataset:")
print(df)

# Top 5 players by goals
print("\nTop 5 Players with Highest Goals:")
top_goals = df.sort_values(
    by="Goals", ascending=False
).head(5)

print(top_goals[["Name", "Goals"]])

# Top 5 players by salary
print("\nTop 5 Players with Highest Salaries:")
top_salary = df.sort_values(
    by="Weekly_Salary", ascending=False
).head(5)

print(top_salary[["Name", "Weekly_Salary"]])

# Calculate average age
average_age = df["Age"].mean()

print("\nAverage Age of Players:", round(average_age, 2))

# Players above average age
print("\nPlayers Above Average Age:")
above_average = df[df["Age"] > average_age]

print(above_average[["Name", "Age"]])

# Visualize player positions
position_count = df["Position"].value_counts()

plt.figure(figsize=(7, 5))
position_count.plot(kind="bar")

plt.title("Distribution of Soccer Players by Position")
plt.xlabel("Player Position")
plt.ylabel("Number of Players")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()