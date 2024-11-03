import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ticker = 'AAPL' 
data = yf.download(ticker, start='2020-10-14', end='2024-10-14')
 

print(data.head())
data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()
print(data.tail())
data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()
print(data.tail())
data['Daily_Return'] = data['Close'].pct_change() 
print(data[['Close', 'Daily_Return']].head())

plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['50_MA'], label='50-Day MA', color='red')
plt.plot(data['200_MA'], label='200-Day MA', color='green')
plt.title(f'{ticker} Stock Price and Moving Averages')
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(data['Daily_Return'].dropna(), bins=100, color='purple')
plt.title(f'{ticker} Daily Returns Distribution')
plt.show()



