import pandas as pd
import yfinance as yf

# Function to fetch market cap data for a specific stock
def fetch_market_cap(ticker):
    stock = yf.Ticker(ticker)
    market_cap = stock.info["marketCap"]
    return market_cap

# Load the S&P 500 symbol list (replace the filename with your actual file location)
# symbol_list = pd.read_csv("sp500_symbols.csv")["Symbol"].tolist()
# symbol_list = pd.read_csv("stock_symbols.csv")["Symbol"].tolist()
symbol_list = pd.read_csv("stock_symbol_NASDAQ100.csv")["Ticker"].tolist()

# Fetch market cap data for each stock in the list
market_caps = []
for symbol in symbol_list:
    try:
        market_cap = fetch_market_cap(symbol)
        market_caps.append([symbol, market_cap])
    except Exception as e:
        print(f"Error fetching market cap for {symbol}: {e}")

# Convert the market_caps list to a DataFrame and sort it by market cap (descending)
market_caps_df = pd.DataFrame(market_caps, columns=["Symbol", "MarketCap"])
market_caps_df = market_caps_df.sort_values("MarketCap", ascending=False)

# Display the top 50 companies by market cap
print("Top 50 Companies by Market Cap:")
print(market_caps_df.head(50))