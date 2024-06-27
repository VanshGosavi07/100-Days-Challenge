import requests
from datetime import datetime

today = datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"
username = 'vanshgosavi'
token = "1066391112"
user_params = {
    'token': token,
    'username': username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph1"
graph_params = {
    'id': graph_id,
    'name': "Coding Graph",
    'unit': 'min',
    'type': 'int',
    'color': 'shibafu',
}
headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph_pixels_endpoint = f"{graph_endpoint}/{graph_id}"

graph_pixels_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': "65"
}
# response = requests.post(url=graph_pixels_endpoint, json=graph_pixels_params, headers=headers)
# print(response.text)

put_endpoint = f"{pixela_endpoint} /{username}/graphs/{graph_id} /{today.strftime('%Y%m%d')}"
put_params = {
    'quantity': '55'
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint = put_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
