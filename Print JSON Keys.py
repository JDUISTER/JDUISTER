import pandas as pd
import requests
import json

url = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_data = json.loads(response.text)
    # data = response.json()
    print('Success')
else:
    print(f"Failed to retrieve data, status code: {response.status_code}")

def print_json_keys(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + f"{key}")
            print_json_keys(value, indent + 1)
    elif isinstance(data, list):
        if data:
            print('  ' * indent + f"[List of {len(data)} items]")
            print_json_keys(data[0], indent + 1)

df = pd.json_normalize(json_data)

df = pd.json_normalize(data['events'])
