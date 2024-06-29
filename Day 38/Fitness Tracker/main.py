from datetime import datetime
import requests
import os

# Get exercise input from the user
query = input("Tell me which exercise you did: \n")

# Nutritionix API credentials
api = "95378b8a50114a7f63827b647f6ed902"
api_id = "fc406e66"

# Nutritionix API endpoint and headers
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": api_id,
    "x-app-key": api
}

# Body for the Nutritionix API request
body = {
    "query": query,
    "gender": "Male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 19
}

# Send the POST request to Nutritionix API
response = requests.post(url, headers=headers, json=body)
response.raise_for_status()
result = response.json()
print(result)

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety API endpoint
sheet_endpoint = 'https://api.sheety.co/91dfe451e9dae274844456eaf2e1c6fc/data/workouts'

# Body for the Sheety API request
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
