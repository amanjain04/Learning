import yfinance as yf

# Replace with your stock symbol
ticker = "RELIANCE.NS"

# Fetch last 1 day of 1-minute interval data
data = yf.download(ticker, interval="1m", period="1d")

# Print the latest 5 rows
print(data.tail())