import json

data_list = []

with open("posts.json", "r") as file:
    x = file.read()
    finaldataclasses = json.loads(x)
    data_list.append(finaldataclasses)
meter_ids_less_than_28 = []
for data in data_list:
    for key,unit in data.items():
        daily_consumption = data.get("daily", [])
        if len(daily_consumption) < 28:
            meter_ids_less_than_28.append(key)

print("Meter IDs with consumption < 28 days:")
for meter_data in meter_ids_less_than_28:
    meter_id = list(meter_data.keys())[0]  # Extract the meter ID
    print(meter_id)

