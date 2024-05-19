!pip install yfinance mplfinance tqdm
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime, timedelta
from tqdm.notebook import tqdm
import time
def download_with_delay(ticker, start, end, interval, delay=0.25):
    try:
        data = yf.download(ticker, start=start, end=end, interval=interval)
        time.sleep(delay)  # Introduce a delay between requests
        return data
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
        return None
        def aggregate_ticks(df, tick_size):
    df['Tick_Group'] = (np.arange(len(df)) // tick_size)
    aggregated = df.groupby('Tick_Group').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    }).reset_index(drop=True)
    return aggregated
    def plot_candlestick(df, title):
    df.index = pd.date_range(start=datetime.now(), 
    def update_chart_incrementally(ticker, start_date, end_date):
    current_date = start_date
    all_data = pd.DataFrame()

    while current_date <= end_date:
        next_date = current_date + timedelta(days=1)
        data = download_with_delay(ticker, start=current_date.strftime('%Y-%m-%d'), end=next_date.strftime('%Y-%m-%d'), interval="5m", delay=0.25)

        if data is not None and not data.empty:
            all_data = pd.concat([all_data, data])
            tick_100 = aggregate_ticks(all_data, 100)
            
        current_date = next_date

    # Plot the final 100-tick candlestick chart
    plot_candlestick(tick_100, f'100 Tick Aggregated Data for {ticker} up to {end_date.strftime("%Y-%m-%d")}')
        
# Run the main function
ticker = "DXYZ"
start_date = datetime(2024, 3, 26)
end_date = datetime(2024, 5, 17)

update_chart_incrementally(ticker, start_date, end_date)periods=len(df), freq='T')
    df = df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    mpf.plot(df, type='candle', style='charles', title=title, volume=True, 
             figratio=(12, 6), figscale=1.2, tight_layout=True, 
             xrotation=20, ylabel='Price', ylabel_lower='Volume')
