import requests
import json

# Fetch CoinMarketCap Data
def fetch_coinmarketcap_data(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        bitcoin_data = next(item for item in data['data'] if item['symbol'] == 'BTC')
        
        # Return necessary data as a dictionary
        return {
            'price': bitcoin_data['quote']['USD']['price'],
            'market_cap': bitcoin_data['quote']['USD']['market_cap'],
            'volume': bitcoin_data['quote']['USD']['volume_24h'],
            'circulating_supply': bitcoin_data['circulating_supply'],
            'percent_change_1h': bitcoin_data['quote']['USD']['percent_change_1h'],
            'percent_change_24h': bitcoin_data['quote']['USD']['percent_change_24h'],
            'percent_change_7d': bitcoin_data['quote']['USD']['percent_change_7d']
        }
    else:
        print("Failed to fetch CoinMarketCap data")
        return None

# Fetch CoinGecko Data
def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'volume': data['market_data']['total_volume']['usd'],
            'percent_change_1h': data['market_data']['price_change_percentage_1h_in_currency']['usd'],
            'percent_change_24h': data['market_data']['price_change_percentage_24h_in_currency']['usd'],
            'percent_change_7d': data['market_data']['price_change_percentage_7d_in_currency']['usd']
        }
    else:
        print("Failed to fetch CoinGecko data")
        return None

# Fetch Binance Data
def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': float(data['lastPrice']),
            '24h_change': float(data['priceChangePercent']),
            'volume': float(data['volume']),
            'quote_volume': float(data['quoteVolume'])
        }
    else:
        print("Failed to fetch Binance data")
        return None

# Fetch Kraken Data
def fetch_kraken_data():
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': float(data['result']['XXBTZUSD']['c'][0]),
            'volume': float(data['result']['XXBTZUSD']['v'][0])
        }
    else:
        print("Failed to fetch Kraken data")
        return None

# Prepare the data for the prediction model
def prepare_model_data():
    coinmarketcap_api_key = "88e17407-d0c9-4b62-9e9b-ff4a213291f3"  # Replace with your actual key
    
    # Fetch data from all platforms
    coinmarketcap_data = fetch_coinmarketcap_data(coinmarketcap_api_key)
    coingecko_data = fetch_coingecko_data()
    binance_data = fetch_binance_data()
    kraken_data = fetch_kraken_data()

    if not coinmarketcap_data or not coingecko_data or not binance_data or not kraken_data:
        return None  # If data fetching failed
    
    # Combine data from all platforms into a single dictionary
    model_data = {
        'coinmarketcap': {
            'price': coinmarketcap_data['price'],
            'market_cap': coinmarketcap_data['market_cap'],
            'volume': coinmarketcap_data['volume'],
            'circulating_supply': coinmarketcap_data['circulating_supply'],
            'percent_change_1h': coinmarketcap_data['percent_change_1h'],
            'percent_change_24h': coinmarketcap_data['percent_change_24h'],
            'percent_change_7d': coinmarketcap_data['percent_change_7d']
        },
        'coingecko': {
            'price': coingecko_data['price'],
            'market_cap': coingecko_data['market_cap'],
            'volume': coingecko_data['volume'],
            'percent_change_1h': coingecko_data['percent_change_1h'],
            'percent_change_24h': coingecko_data['percent_change_24h'],
            'percent_change_7d': coingecko_data['percent_change_7d']
        },
        'binance': {
            'price': binance_data['price'],
            '24h_change': binance_data['24h_change'],
            'volume': binance_data['volume'],
            'quote_volume': binance_data['quote_volume']
        },
        'kraken': {
            'price': kraken_data['price'],
            'volume': kraken_data['volume']
        }
    }
    
    return model_data

# Function to make prediction with Ollama model
def make_prediction_with_ollama(model_data):
    api_url = "http://localhost:11434/api/generate"  # Replace with the actual URL if different
    model_name = "deepseek-r1:1.5b"  # Replace with your model name

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_name,
        "prompt": f"Predict Bitcoin's future price based on the following data: {json.dumps(model_data)}",
        "stream": False  # Set to False for non-streaming response
    }

    try:
        # Send POST request to Ollama API
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

# Main function to fetch data from all APIs and make predictions
def fetch_all_bitcoin_data():
    # Prepare the model input data
    model_data = prepare_model_data()
    
    if model_data:
        # Make prediction
        prediction = make_prediction_with_ollama(model_data)
        if prediction:
            print("\n--- Model Prediction ---")
            print(f"Prediction: {prediction}")
        else:
            print("Prediction failed.")
    else:
        print("Model data preparation failed.")

if __name__ == "__main__":
    fetch_all_bitcoin_data()
