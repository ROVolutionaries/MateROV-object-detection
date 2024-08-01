import json
import os

json_file_path = "data.json"

with open(json_file_path, "r") as file:
    data = json.load(file)

filtered_data = [entry for entry in data if 'width' in entry and 'height' in entry]

with open(json_file_path, "w") as file:
    json.dump(filtered_data, file, indent=4)

print(f"Updated JSON file saved to {json_file_path}.")
