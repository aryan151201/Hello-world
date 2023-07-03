import json
import os

def read_json_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                data_list.append(data)
    return data_list

directory_path = 'C:\\Users\\ASUS\\Downloads'
json_data = read_json_files(directory_path)
meter_ids_less_than_28 = []
for data in json_data:
    daily_consumption = data.get("daily", [])
    if len(daily_consumption) < 28:
        meter_ids_less_than_28.append(data)

print("Meter IDs with consumption < 28 days:")
for meter_data in meter_ids_less_than_28:
    meter_id = list(meter_data.keys())[0]  # Extract the meter ID
    print(meter_id)
