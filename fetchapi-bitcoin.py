import requests
import json

# CoinGecko API - Bitcoin general data
def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\n--- CoinGecko Data ---")
        print(f"Price: ${data['market_data']['current_price']['usd']}")
        print(f"Market Cap: ${data['market_data']['market_cap']['usd']}")
        print(f"24h Volume: ${data['market_data']['total_volume']['usd']}")
    else:
        print("Failed to fetch CoinGecko data")

# Binance API - Bitcoin trading data
def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\n--- Binance Data ---")
        print(f"Price: ${data['lastPrice']}")
        print(f"24h Change: {data['priceChangePercent']}%")
        print(f"24h Volume: {data['volume']} BTC")
        print(f"24h Quote Volume: ${data['quoteVolume']}")
    else:
        print("Failed to fetch Binance data")

# Kraken API - Bitcoin trading data
def fetch_kraken_data():
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\n--- Kraken Data ---")
        print(f"Price: ${data['result']['XXBTZUSD']['c'][0]}")
        print(f"24h Volume: {data['result']['XXBTZUSD']['v'][0]} BTC")
    else:
        print("Failed to fetch Kraken data")

# CoinMarketCap API - Bitcoin general market data
def fetch_coinmarketcap_data(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        bitcoin_data = next(item for item in data['data'] if item['symbol'] == 'BTC')
        print("\n--- CoinMarketCap Data ---")
        print(f"Name: {bitcoin_data['name']}")
        print(f"Price: ${bitcoin_data['quote']['USD']['price']}")
        print(f"Market Cap: ${bitcoin_data['quote']['USD']['market_cap']}")
        print(f"24h Volume: ${bitcoin_data['quote']['USD']['volume_24h']}")
        print(f"Circulating Supply: {bitcoin_data['circulating_supply']}")
        # Remove market_cap_by_total_supply or add a check to avoid errors
        if 'market_cap_by_total_supply' in bitcoin_data:
            print(f"Market Cap by Total Supply: ${bitcoin_data['market_cap_by_total_supply']}")
        else:
            print("Market Cap by Total Supply: Not Available")
        print(f"Change in 1h: {bitcoin_data['quote']['USD']['percent_change_1h']}%")
        print(f"Change in 24h: {bitcoin_data['quote']['USD']['percent_change_24h']}%")
        print(f"Change in 7d: {bitcoin_data['quote']['USD']['percent_change_7d']}%")
    else:
        print("Failed to fetch CoinMarketCap data")

# Main function to fetch data from all APIs
def fetch_all_bitcoin_data():
    # Fetch CoinMarketCap API Key
    coinmarketcap_api_key = "88e17407-d0c9-4b62-9e9b-ff4a213291f3"  # Replace with your actual key
    
    # Call all the functions to fetch data
    fetch_coingecko_data()
    fetch_binance_data()
    fetch_kraken_data()
    fetch_coinmarketcap_data(coinmarketcap_api_key)

if __name__ == "__main__":
    fetch_all_bitcoin_data()
