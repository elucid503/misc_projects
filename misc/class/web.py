import requests

api_url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"
response = requests.get(api_url)
data = response.json()

for p in data.get("results"):
    print("Pokemon name:", p.get("name"))