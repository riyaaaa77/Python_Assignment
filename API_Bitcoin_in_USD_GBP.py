#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
data_points = {}  # Dictionary to store the data points

# Set the start and end timestamps for 1 day
start_timestamp = int(time.time())
end_timestamp = start_timestamp + (24 * 60 * 60)

# Collect data at 5-minute intervals
current_timestamp = start_timestamp
while current_timestamp < end_timestamp:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_price = data['bpi']['USD']['rate']
        gbp_price = data['bpi']['GBP']['rate']
        
        # Store unique data points
        if usd_price not in data_points.values() and gbp_price not in data_points.values():
            data_points[current_timestamp] = {'USD': usd_price, 'GBP': gbp_price}
        
        current_timestamp += 300  # Add 5 minutes (in seconds)
        time.sleep(5)  # Pause execution for 5 seconds to avoid rate limiting

# Print the collected data points
for timestamp, prices in data_points.items():
    print(f"Timestamp: {timestamp}, USD Price: {prices['USD']}, GBP Price: {prices['GBP']}")


# In[ ]:


import requests
import time

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
data_points = {}  # Dictionary to store the data points
lowest_price = float('inf')  # Initialize with a very high value
highest_price = float('-inf')  # Initialize with a very low value

# Set the start and end timestamps for 1 day
start_timestamp = int(time.time())
end_timestamp = start_timestamp + (24 * 60 * 60)

# Collect data at 5-minute intervals
current_timestamp = start_timestamp
while current_timestamp < end_timestamp:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_price = float(data['bpi']['USD']['rate'].replace(',', ''))
        gbp_price = float(data['bpi']['GBP']['rate'].replace(',', ''))
        
        # Store unique data points
        if usd_price not in data_points.values() and gbp_price not in data_points.values():
            data_points[current_timestamp] = {'USD': usd_price, 'GBP': gbp_price}
            
            # Check for lowest price
            if usd_price < lowest_price:
                lowest_price = usd_price
            if gbp_price < lowest_price:
                lowest_price = gbp_price
            
            # Check for highest price
            if usd_price > highest_price:
                highest_price = usd_price
            if gbp_price > highest_price:
                highest_price = gbp_price
        
        current_timestamp += 300  # Add 5 minutes (in seconds)
        time.sleep(5)  # Pause execution for 5 seconds to avoid rate limiting

# Print the collected data points
for timestamp, prices in data_points.items():
    print(f"Timestamp: {timestamp}, USD Price: {prices['USD']}, GBP Price: {prices['GBP']}")

# Print the highest and lowest prices
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}"

