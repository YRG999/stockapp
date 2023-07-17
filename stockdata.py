import yfinance as yf

def download_stock_data(symbol, start_date, engitd_date):
    # Download stock data
    data = yf.download(symbol, start=start_date, end=end_date)

    # Save data to a CSV file
    filename = f"{symbol}_stock_data.csv"
    data.to_csv(filename)

    print(f"Stock data for {symbol} has been downloaded and saved to {filename}.")

# # Example usage
# symbol = "AAPL"  # Stock symbol (e.g., Apple Inc.)
# start_date = "2023-01-01"  # Start date for data retrieval
# end_date = "2023-07-09"  # End date for data retrieval

# # SPY
# symbol = "SPY"  # Stock symbol (e.g., Apple Inc.)
# start_date = "2020-01-01"  # Start date for data retrieval
# end_date = "2023-07-09"  # End date for data retrieval

# MSFT
symbol = "MSFT"  # Stock symbol (e.g., Apple Inc.)
start_date = "2013-01-01"  # Start date for data retrieval
end_date = "2023-07-12"  # End date for data retrieval

download_stock_data(symbol, start_date, end_date)
