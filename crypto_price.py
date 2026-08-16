import requests

coin = input("Enter cryptocurrency (bitcoin/ethereum): ").lower()

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": coin,
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

if coin in data:
    price = data[coin]["usd"]
    print("\n--- CRYPTOCURRENCY PRICE ---")
    print("Cryptocurrency:", coin)
    print("Current price: $", price)
else:
    print("Cryptocurrency not found.")