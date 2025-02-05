import requests
import json

# CoinMarketCap API - Fetch ADA general data
def fetch_coinmarketcap_data(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'X-CMC_PRO_API_KEY': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        ada_data = next(item for item in data['data'] if item['symbol'] == 'ADA')
        
        return {
            'price': ada_data['quote']['USD']['price'],
            'market_cap': ada_data['quote']['USD']['market_cap'],
            'volume': ada_data['quote']['USD']['volume_24h'],
            'circulating_supply': ada_data['circulating_supply'],
            'percent_change_1h': ada_data['quote']['USD']['percent_change_1h'],
            'percent_change_24h': ada_data['quote']['USD']['percent_change_24h'],
            'percent_change_7d': ada_data['quote']['USD']['percent_change_7d']
        }
    else:
        print("Failed to fetch CoinMarketCap data")
        return None

# CoinGecko API - ADA general data
def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/cardano"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'volume': data['market_data']['total_volume']['usd']
        }
    else:
        print("Failed to fetch CoinGecko data")
        return None

# Binance API - ADA/USDT trading data
def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=ADAUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['lastPrice'],
            'percent_change_24h': data['priceChangePercent'],
            'volume': data['volume'],
            'quote_volume': data['quoteVolume']
        }
    else:
        print("Failed to fetch Binance data")
        return None

# Kraken API - ADA trading data
def fetch_kraken_data():
    url = "https://api.kraken.com/0/public/Ticker?pair=ADAUSD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['result']['ADAUSD']['c'][0],
            'volume': data['result']['ADAUSD']['v'][0]
        }
    else:
        print("Failed to fetch Kraken data")
        return None

# Function to prepare data for model prediction
def prepare_model_data():
    coinmarketcap_api_key = "88e17407-d0c9-4b62-9e9b-ff4a213291f3"  # Replace with your actual key
    
    # Fetch data from all APIs
    coinmarketcap_data = fetch_coinmarketcap_data(coinmarketcap_api_key)
    coingecko_data = fetch_coingecko_data()
    binance_data = fetch_binance_data()
    kraken_data = fetch_kraken_data()
    
    if not all([coinmarketcap_data, coingecko_data, binance_data, kraken_data]):
        print("Failed to fetch data from one or more platforms.")
        return None
    
    # Combine the data into a single dictionary for the model
    model_data = {
        'coinmarketcap': coinmarketcap_data,
        'coingecko': coingecko_data,
        'binance': binance_data,
        'kraken': kraken_data
    }
    
    return model_data

# Function to make prediction with Ollama model
def make_prediction_with_ollama(model_data):
    api_url = "http://localhost:11434/api/generate"  # Replace with the actual URL if different
    model_name = "deepseek-r1:1.5b"  # Replace with your model name

    headers = {
        "Content-Type": "application/json"
    }

    # Define the instruction for the model
    instruction = (
        "You are an AI trained to predict ADA's future price based on historical and real-time data. "
        "The following data comes from different platforms that track ADA's price, market cap, volume, and other metrics. "
        "Consider the changes in price, volume, and market trends across different platforms (CoinMarketCap, CoinGecko, Binance, Kraken) "
        "to make an informed prediction about ADA/USDT's future price. "
        "Use the provided data to predict the price of ADA within the next 24 hours, based on the current trends."
    )

    # Create the prompt by combining instruction and model data
    payload = {
        "model": model_name,
        "prompt": f"{instruction}\n\nHere is the data from different sources: {json.dumps(model_data)}\n\nBased on this data, predict ADA/USDT's future price:",
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
def fetch_all_ada_data():
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
    fetch_all_ada_data()
