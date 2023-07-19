import yfinance as yf

def fetch_market_cap(ticker):
    """
    Fetches market cap data for a specific stock.

    Parameters:
    - ticker (str): The stock to get market cap data from.

    Returns:
    - str: The market cap of the stock.
    """
    stock = yf.Ticker(ticker)
    market_cap = stock.info["marketCap"]
    return market_cap

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches stock data for a specific stock.

    Parameters:
    - ticker (str): The stock to get data from.
    - start_date (str): The start date, in YYYY-MM-DD format.
    - end_date (str): The end date, in YYYY-MM-DD format.

    Returns:
    - str: The stock history data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def download_stock_data(symbol, start_date, end_date):
    """
    Downloads stock data, save to CSV, and prints filename.

    Parameters:
    - symbol (str): The stock symbol, e.g. "AAPL"
    - start_date (str): Start date for data retrieval, e.g. "2023-01-01"
    - end_date (str): End date for data retieval, e.g. "2023-07-09"
    """
    data = yf.download(symbol, start=start_date, end=end_date)
    filename = f"{symbol}_stock_data.csv"
    data.to_csv(filename)
    print(f"Stock data for {symbol} has been downloaded and saved to {filename}.")