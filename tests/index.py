import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas

import yfinance as yf
import time


def getstock(ticker):
    tickers = [ticker]
    for ticker in tickers:
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        
        time.sleep(1)
        
        new_quote = data['Close'].iloc[-1]
        
        if (new_quote > last_quote):
            print("UP")
        elif (new_quote < last_quote):
            print("DOWN")
        elif (new_quote == last_quote):
            print("NO_CHANGE")
        return last_quote



while True:
    print(getstock("BTC-USD"))
    time.sleep(1)