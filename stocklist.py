# stocklist3.py

import pandas as pd

url = "https://en.wikipedia.org/wiki/Nasdaq-100"

# Read the tables from the URL
tables = pd.read_html(url)

# Find the table with stock symbols
djia_table = None
for table in tables:
    if "Ticker" in table.columns:
        djia_table = table
        break

if djia_table is None:
    print("Could not find the table with stock symbols.")
else:
    # Clean up the table
    djia_table = djia_table[['Ticker']]
    
    # Save the stock symbols and company names to a CSV file
    djia_table.to_csv("stock_symbol_NASDAQ100.csv", index=False)
    print("Stock symbols have been saved to 'stock_symbol_NASDAQ100.csv'.")