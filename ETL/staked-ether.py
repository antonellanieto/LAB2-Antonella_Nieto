import requests
import csv


url = 'https://api.coingecko.com/api/v3/coins/staked-ether/market_chart/range?vs_currency=usd&from=1420081200&to=1672542000'




params = {
    "vs_currency": "usd",
    "from": 1420081200,  # Unix timestamp for the "from" date
    "to": 1672542000    # Unix timestamp for the "to" date
}


response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    prices = data["prices"]
    

    with open("staked-ether_data.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Timestamp", "Price"])
        
        for entry in prices:
            timestamp = entry[0] / 1000  # Convert from milliseconds to seconds
            price = entry[1]
            csv_writer.writerow([timestamp, price])
        
    print("CSV file created successfully.")
else:
    print("Failed to retrieve data:", response.status_code)