import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=20" # 20 pokemons
response = requests.get(api_url)
data = response.json()

cards = []

for p in data.get("results"):

    moreinfo = requests.get(p.get("url"))
    moredata = moreinfo.json()

    if (not moredata.get("name")):
        continue
    
    pokemon_card = { 

        "name": p.get("name"),
        
        "type": moredata.get("types")[0].get("type").get("name"),

        "moves": [ moredata.get("moves")[0].get("move").get("name") ],

        "abilities": [ moredata.get("abilities")[0].get("ability").get("name") ]

    }

    cards.append(pokemon_card)

# Print 

print(json.dumps(cards, indent=2))

# Write to file

with open("cards.json", "w") as f:
    json.dump(cards, f, indent=2)