import requests

api_url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"
response = requests.get(api_url)
data = response.json()

cards = []

for p in data.get("results"):

    print(p.get("name"), end=": ")
    print(p.get("url"), end = "\n")

    moreinfo = requests.get(p.get("url"))
    moredata = moreinfo.json()

    for sprite in moredata.get("sprites").items():
        print(sprite[0], ": ", sprite[1])

    pokemon_card = { 

        "name": p.get("name"),
        "url": p.get("url"),

        "height": moredata.get("height"),
        "weight": moredata.get("weight"),

        "hp": moredata.get("stats")[0].get("base_stat"),
        "attack": moredata.get("stats")[1].get("base_stat"),
        "defense": moredata.get("stats")[2].get("base_stat"),

        "speed": moredata.get("stats")[5].get("base_stat"),

    }

    cards.append(pokemon_card)

print(cards)
