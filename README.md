# Stock apps

* `stockcomparison.py` -- compare stock prices for 120 days from today and the same time period a year ago.
* `marketcap.py` -- get marketcap for all stocks in a list.
* `stocklist.py` -- get the list of stocks in the NASDAQ100 list.
* `stockdata.py` -- download daily stock data from Yahoo Finance.
* `stockpredict.py` -- use a [long short-term memory network (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory) to predict stock prices.
* `comparemonths.py` -- compare stock data month over month for a stock from a list of daily stock data.

## Set up env

Create & activate new virtual environment

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

The following will be installed.

<details>
  <summary>Full package list</summary>

```
appdirs            1.4.4
beautifulsoup4     4.12.2
certifi            2023.5.7
cffi               1.15.1
charset-normalizer 3.1.0
contourpy          1.1.0
cryptography       41.0.1
cycler             0.11.0
fonttools          4.40.0
frozendict         2.3.8
html5lib           1.1
idna               3.4
kiwisolver         1.4.4
lxml               4.9.2
matplotlib         3.7.1
multitasking       0.0.11
numpy              1.24.3
packaging          23.1
pandas             2.0.2
Pillow             9.5.0
pip                23.1.2
pycparser          2.21
pyparsing          3.0.9
python-dateutil    2.8.2
pytz               2023.3
requests           2.31.0
setuptools         58.1.0
six                1.16.0
soupsieve          2.4.1
tzdata             2023.3
urllib3            2.0.3
webencodings       0.5.1
yfinance           0.2.20
```

</details>