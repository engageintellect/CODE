import yfinance as yf
from datetime import date

today = date.today()

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', end=today)

#see your data
data = str(tickerDf)

print(data)
# print(data.split('\n'))
