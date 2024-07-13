import requests

response = requests.get(url=f"https://api.npoint.io/beed84b243f025b8b61c")
response.raise_for_status()
print(response.json())

