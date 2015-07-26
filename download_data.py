# Import data reader and time reader
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

# Import library
import pandas as pd

# Downloading data from Yahoo.com on KLK (2445.KL)
start = dt(2011,6,1)
end = dt(2015,6,1)
data = DR("2445.KL", 'yahoo', start, end)

# Calculate mean for 5-day moving average for every 5 days
data['5-day Moving Average'] = pd.rolling_mean(data['Close'],5)

# Downloading KLSE data and computing correlation
KLSEdata = DR("^KLSE", 'yahoo', start, end)
cor_data = ['^KLSE','2445.KL']
closing = DR(cor_data,'yahoo',start,end)['Close']
correlation = closing.corr()
printer = correlation['^KLSE']
print("Correlation coefficient of Kuala Lumpur Stock Exchange and Kuala Lumpur Kepong is",printer['2445.KL'])
if printer['2445.KL'] > 0:
    print('Kuala Lumpur Stock Exchange (KLSE) and Kuala Lumpur Kepong (2445.KL) are positively correlated.')
else:
    print('Kuala Lumpur Stock Exchange (KLSE) and Kuala Lumpur Kepong (2445.KL) are negatively correlated.')
    
# Plot the graph
data['5-day Moving Average'].plot(title = 'Moving Average of Stock Prices from June 2011 to May 2015 of Kuala Lumpur Kepong (2445.KL)', color='r')