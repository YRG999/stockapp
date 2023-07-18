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
Package                 Version
----------------------- --------
absl-py                 1.4.0
appdirs                 1.4.4
astunparse              1.6.3
beautifulsoup4          4.12.2
cachetools              5.3.1
certifi                 2023.5.7
charset-normalizer      3.2.0
contourpy               1.1.0
cycler                  0.11.0
flatbuffers             23.5.26
fonttools               4.41.0
frozendict              2.3.8
gast                    0.4.0
google-auth             2.22.0
google-auth-oauthlib    1.0.0
google-pasta            0.2.0
grpcio                  1.56.0
h5py                    3.9.0
html5lib                1.1
idna                    3.4
joblib                  1.3.1
keras                   2.13.1
kiwisolver              1.4.4
libclang                16.0.6
lxml                    4.9.3
Markdown                3.4.3
MarkupSafe              2.1.3
matplotlib              3.7.2
multitasking            0.0.11
numpy                   1.24.3
oauthlib                3.2.2
opt-einsum              3.3.0
packaging               23.1
pandas                  2.0.3
Pillow                  10.0.0
pip                     23.2
protobuf                4.23.4
pyasn1                  0.5.0
pyasn1-modules          0.3.0
pyparsing               3.0.9
python-dateutil         2.8.2
pytz                    2023.3
requests                2.31.0
requests-oauthlib       1.3.1
rsa                     4.9
scikit-learn            1.3.0
scipy                   1.11.1
setuptools              58.1.0
six                     1.16.0
soupsieve               2.4.1
tensorboard             2.13.0
tensorboard-data-server 0.7.1
tensorflow              2.13.0
tensorflow-estimator    2.13.0
tensorflow-macos        2.13.0
termcolor               2.3.0
threadpoolctl           3.2.0
typing_extensions       4.5.0
tzdata                  2023.3
urllib3                 1.26.16
webencodings            0.5.1
Werkzeug                2.3.6
wheel                   0.40.0
wrapt                   1.15.0
yfinance                0.2.24
```

</details>

Uninstall all pip packages

```bash
$ pip uninstall -y -r <(pip freeze)
```

A note on `sklearn` vs `scikit-learn`: https://towardsdatascience.com/scikit-learn-vs-sklearn-6944b9dc1736