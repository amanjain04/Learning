import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from datetime import datetime

def fetch_nifty50_data():
    """
    Fetch the historical data for Nifty 50 index.
    Returns a DataFrame containing the data.
    """
    try:
        # Replace '^NSEI' with the ticker symbol of Nifty 50 for your data provider
        nifty_data = yf.download('^NSEI', period='1mo', interval='1d')  
        return nifty_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_rsi(data, period=14):
    """
    Calculate the RSI for the given data.
    :param data: DataFrame containing historical data with 'Close' prices.
    :param period: RSI period (default is 14).
    :return: RSI series.
    """
    rsi_indicator = RSIIndicator(data['Close'], window=period)
    return rsi_indicator.rsi()

def notify_if_rsi_below_threshold(rsi, threshold=50):
    """
    Notify the user if RSI is below the given threshold.
    :param rsi: RSI series.
    :param threshold: Threshold for notification.
    """
    current_rsi = rsi.iloc[-1]  # Get the latest RSI value
    if current_rsi < threshold:
        print(f"Alert! RSI is below {threshold}: Current RSI = {current_rsi:.2f}")
    else:
        print(f"RSI is above {threshold}: Current RSI = {current_rsi:.2f}")

def main():
    # Fetch data
    data = fetch_nifty50_data()
    if data is not None:
        # Calculate RSI
        data['RSI'] = calculate_rsi(data)
        # Notify user
        notify_if_rsi_below_threshold(data['RSI'])
    else:
        print("Failed to fetch data. Exiting.")

if __name__ == "__main__":
    main()
