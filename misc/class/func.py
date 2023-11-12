import requests

def get_data(data_url):
    response = requests.get(data_url)
    return response.json()

def create_a_card(p_data):
    p_card = {
        "name": p_data.get("name"),
        "abilities": [ability["ability"]["name"] for ability in p_data.get("abilities", [])],
        "moves": [move["move"]["name"] for move in p_data.get("moves", [])],
        "types": [ptype["type"]["name"] for ptype in p_data.get("types", [])]
    }
    return p_card

def pretty_print_pokemon(pokemon_card):
    print(f"Name: {pokemon_card['name']}")
    print("Abilities:", ", ".join(pokemon_card["abilities"]))
    print("Moves:", ", ".join(pokemon_card["moves"]))
    print("Types:", ", ".join(pokemon_card["types"]))

p_url = "https://pokeapi.co/api/v2/pokemon?limit=3&offset=0"
data = get_data(p_url)

p_deck_list = []
for p in data.get("results", []):
    p_data = get_data(p.get("url"))
    p_card = create_a_card(p_data)
    p_deck_list.append(p_card)

# Print all Pokemon cards in the deck
for card in p_deck_list:
    pretty_print_pokemon(card)
    print("*****************************")
