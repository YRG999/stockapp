# stockcomp3.py

import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

# Specify your stock symbol and the time periods to compare
stock_symbol = "AAPL"
current_start_date = datetime.now() - timedelta(days=120)
current_end_date = datetime.now()
previous_start_date = current_start_date - timedelta(days=365)
previous_end_date = current_end_date - timedelta(days=365)

current_data = fetch_stock_data(stock_symbol, current_start_date, current_end_date)
previous_data = fetch_stock_data(stock_symbol, previous_start_date, previous_end_date)

# Normalize the stock data by dividing each value by the starting value
current_data["Normalized"] = current_data["Close"] / current_data.iloc[0]["Close"]
previous_data["Normalized"] = previous_data["Close"] / previous_data.iloc[0]["Close"]

# Create new columns representing the number of days elapsed since the beginning of time periods
current_data["Days"] = (current_data.index - current_data.index[0]).days
previous_data["Days"] = (previous_data.index - previous_data.index[0]).days

# Plot the current and previous time periods
plt.figure(figsize=(14, 7))
plt.plot(current_data["Days"], current_data["Normalized"], label="Current Time Period")
plt.plot(previous_data["Days"], previous_data["Normalized"], label="Previous Time Period")
plt.xlabel("Days (Start at 0)")
plt.ylabel("Normalized Price")
plt.title(f"Comparison of {stock_symbol} Stock Price - Current Time Period vs Previous Time Period")
plt.legend()
plt.grid()
plt.show()