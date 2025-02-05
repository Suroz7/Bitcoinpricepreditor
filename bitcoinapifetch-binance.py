import requests
import json

# Binance API endpoint for general market data (24hr stats for Bitcoin)
market_data_url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"

# Binance API endpoint for futures data (Long/Short ratio, Liquidations)
futures_data_url = "https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=1h&limit=1"

# Send request for general market data (price, volume, etc.)
response = requests.get(market_data_url)

if response.status_code == 200:
    market_data = response.json()
    print("Bitcoin Market Data (24hr):")
    print(f"Current Price: ${market_data['lastPrice']}")
    print(f"24h Price Change: {market_data['priceChangePercent']}%")
    print(f"24h Trading Volume: {market_data['volume']} BTC")
    print(f"24h Quote Volume (USD): ${market_data['quoteVolume']}")
    print(f"High Price (24h): ${market_data['highPrice']}")
    print(f"Low Price (24h): ${market_data['lowPrice']}")
else:
    print("Failed to retrieve market data")

# Send request for futures data (long/short ratio, liquidation data)
response_futures = requests.get(futures_data_url)

if response_futures.status_code == 200:
    futures_data = response_futures.json()
    print("\nBitcoin Futures Data (Long/Short Ratio and Liquidations):")
    # Long/Short Ratio
    long_short_ratio = futures_data[0]['longShortRatio']
    print(f"Long/Short Ratio: {long_short_ratio}")
    
    # Liquidation data (last hour)
    liquidation_url = "https://fapi.binance.com/futures/data/liquidationOrders?symbol=BTCUSDT&limit=5"
    liquidation_response = requests.get(liquidation_url)
    
    if liquidation_response.status_code == 200:
        liquidation_data = liquidation_response.json()
        print(f"\nRecent Liquidations (Top 5):")
        for liquidation in liquidation_data:
            print(f"Order ID: {liquidation['orderId']}, Price: ${liquidation['price']}, Side: {liquidation['side']}")
    else:
        print("Failed to retrieve liquidation data")
else:
    print("Failed to retrieve futures data")
