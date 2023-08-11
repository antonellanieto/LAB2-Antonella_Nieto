import requests
import csv
import pandas as pd 

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=true&locale=en'

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "sparkline": True,
    "locale": "en"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    csv_file = 'crypto_data.csv'

    field_names = [
    "id",
    "symbol",
    "name",
    "image",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "fully_diluted_valuation",
    "total_volume",
    "high_24h",
    "low_24h",
    "price_change_24h",
    "price_change_percentage_24h",
    "market_cap_change_24h",
    "market_cap_change_percentage_24h",
    "circulating_supply",
    "total_supply",
    "max_supply",
    "ath",
    "ath_change_percentage",
    "ath_date",
    "atl",
    "atl_change_percentage",
    "atl_date",
    "roi",
    "last_updated",
    "sparkline_in_7d" 
]
    
    # Abrir el archivo
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

       
        writer.writeheader()

        # Escribir la data por fila
        for entry in data:
            writer.writerow(entry)

    print(f" El archivo se guardo: {csv_file}")
else:
    print("Request error", response.status_code)



