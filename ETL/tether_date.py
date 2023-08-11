import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("tether_data.csv")

# Convert Unix timestamps to datetime objects
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

df_bitcoin = df.copy()

df_bitcoin['Date'] = df['Timestamp']

df_bitcoin.to_csv('tether_date', index=False)