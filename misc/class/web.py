import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
response = requests.get(api_url)
data = response.json()

cards = []

counter = 0

for p in data.get("results"):

    moreinfo = requests.get(p.get("url"))
    moredata = moreinfo.json()

    if ((not moredata.get("types") or not moredata.get("moves") or not moredata.get("abilities"))):
        continue

    counter +=1 

    abilities = []

    for a in moredata.get("abilities"):
        abilities.append(a.get("ability").get("name"))

    moves = []

    for m in moredata.get("moves"):
        moves.append(m.get("move").get("name"))
    
    pokemon_card = { 

        "name": p.get("name"),
        
        "type": moredata.get("types")[0].get("type").get("name"),

        "moves": moves,

        "abilities": abilities

    }

    cards.append(pokemon_card)

    print(f"Compiled {counter} pokemons")

# Write to file

with open("cards.json", "w") as f:
    json.dump(cards, f, indent=2)