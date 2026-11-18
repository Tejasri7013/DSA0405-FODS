import pandas as pd
import matplotlib.pyplot as plt

# Sample stock data
data = {
    "Date": [
        "01-11-2026", "02-11-2026", "03-11-2026",
        "04-11-2026", "05-11-2026", "06-11-2026",
        "07-11-2026", "08-11-2026", "09-11-2026",
        "10-11-2026"
    ],
    "Close": [100, 102, 98, 105, 103, 108, 106, 110, 107, 112]
}

df = pd.DataFrame(data)

# Calculate variability
mean_price = df["Close"].mean()
std_price = df["Close"].std()
variance = df["Close"].var()
minimum = df["Close"].min()
maximum = df["Close"].max()
price_range = maximum - minimum
cv = (std_price / mean_price) * 100

# Display results
print("Stock Price Variability Analysis")
print("-----------------------------")
print("Mean Closing Price:", round(mean_price, 2))
print("Standard Deviation:", round(std_price, 2))
print("Variance:", round(variance, 2))
print("Minimum Price:", minimum)
print("Maximum Price:", maximum)
print("Price Range:", price_range)
print("Coefficient of Variation:", round(cv, 2), "%")

# Analyze variability
if cv < 5:
    print("Stock price variability: Low")
elif cv < 15:
    print("Stock price variability: Moderate")
else:
    print("Stock price variability: High")

# Plot stock prices
plt.plot(df["Date"], df["Close"], marker="o")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Closing Price Analysis")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()