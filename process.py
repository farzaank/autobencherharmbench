import json
import csv

# Load the JSON data from the file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Prepare the data for CSV
csv_data = []
for behavior_name, behavior_prompts in data.items():
    for prompt in behavior_prompts:
        csv_data.append({"behavior_name": behavior_name, "behavior_prompt": prompt})

# Write data to a CSV file
with open("output.csv", "w", newline="") as csv_file:
    fieldnames = ["behavior_name", "behavior_prompt"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(csv_data)

print("Data has been successfully written to output.csv")
