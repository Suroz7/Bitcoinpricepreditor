Bitcoin Live Prediction with Ollama Model

This program fetches real-time Bitcoin data from multiple sources (CoinMarketCap, CoinGecko, Binance, Kraken) and sends the data to the Ollama model for predicting Bitcoin's future price.
Requirements:

    Python 3.x
    requests library
    Ollama (API for the prediction model)
    DeepSeek Model (or any other model you choose)

1. Setting up the Environment

    Install Python (if not already installed):
        Download and install Python from the official site: https://www.python.org/downloads/

    Install Required Python Packages:
        Open a terminal/command prompt and install the necessary Python libraries by running the following command:

        pip install requests

    Download and Install Ollama:
        Download and install Ollama from https://ollama.com/.
        Follow the installation instructions on the Ollama website for your operating system.

    Get the DeepSeek Model:
        If you're using the DeepSeek model, make sure you have the model downloaded. Replace the model name in the code ("deepseek-r1:1.5b") with the actual model name if you're using a different model.
        Make sure the model is available and accessible in the Ollama system.

2. Configuration and API Keys

    CoinMarketCap API Key:
        You need a valid CoinMarketCap API key to fetch data from their platform. You can sign up for a free API key at CoinMarketCap.
        Once you have your API key, replace the coinmarketcap_api_key variable in the code:

    coinmarketcap_api_key = "YOUR_COINMARKETCAP_API_KEY"

Ollama API Configuration:

    Make sure the Ollama API is running locally at the default URL (http://localhost:11434) or adjust it if needed in the code:

        api_url = "http://localhost:11434/api/generate"  # Replace with your actual URL if different

3. Running the Program

    Prepare the Program:
        Download the program script and save it to a file, for example, bitcoin_prediction.py.

    Run the Program:
        Open a terminal/command prompt in the directory where bitcoin_prediction.py is saved.
        Run the program using the following command:

        python bitcoin_prediction.py

    Expected Output:
        The program will fetch data from the CoinMarketCap, CoinGecko, Binance, and Kraken APIs.
        It will then send the combined data to the Ollama model for prediction and print the predicted Bitcoin price.

4. Customizing the Model Name

    If you're using a different model, you can replace the model name in the following line:

    model_name = "deepseek-r1:1.5b"  # Replace with your model name

    Make sure to update it with the exact name of the model you want to use.

5. Troubleshooting

    Issue: No Response from Ollama Model:
        Ensure that Ollama is running locally on your machine.
        Check the status of the Ollama API by visiting http://localhost:11434 in your browser.

    Issue: API Key Errors:
        Make sure your CoinMarketCap API key is correctly set and that it is valid.
        If the API key is invalid, you might need to request a new one from CoinMarketCap.

    Issue: Missing Libraries:
        If you get an error like ModuleNotFoundError, make sure to install the required libraries by running:

        pip install requests

6. Additional Features

    You can extend this program to include more APIs or use historical data for deeper analysis.
    If you'd like to adjust the prediction model or use other AI models, you can replace the model and adjust the code accordingly.

7. Important Links

    CoinMarketCap API
    Ollama
    DeepSeek Model

8. Contact/Support
srz.grz@gmail.com
If you encounter any issues or need help, feel free to reach out to the support team or visit the documentation of the APIs and tools you're using.