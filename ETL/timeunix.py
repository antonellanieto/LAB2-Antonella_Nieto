import datetime

# Define the dates
date_str_1 = "2015-01-01"
date_str_2 = "2023-01-01"

# Convert date strings to datetime objects
date_1 = datetime.datetime.strptime(date_str_1, '%Y-%m-%d')
date_2 = datetime.datetime.strptime(date_str_2, '%Y-%m-%d')

# Convert datetime objects to Unix timestamps (seconds since Unix epoch)
timestamp_1 = int(date_1.timestamp())
timestamp_2 = int(date_2.timestamp())

print("Unix timestamp for", date_str_1, ":", timestamp_1)
print("Unix timestamp for", date_str_2, ":", timestamp_2)