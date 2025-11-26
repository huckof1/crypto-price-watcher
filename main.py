import requests

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return float(response.json()["price"])
    except Exception:
        return "—"

if __name__ == "__main__":
    btc = get_price("BTCUSDT")
    eth = get_price("ETHUSDT")
    
    print("Текущие цены (Binance):")
    print(f"Bitcoin (BTC):   ${btc}")
    print(f"Ethereum (ETH):  ${eth}")
