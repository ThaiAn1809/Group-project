import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Faild to retrieve data {response.status_code}")
    

pok_name = "pikachu"
pok_info = get_pokemon_info(pok_name)

if pok_info:
    print(f"Name: {pok_info["name"].capitalize()}")
    print(f"Id: {pok_info["id"]}")
    print(f"Height: {pok_info["height"]}")
    print(f"Weight: {pok_info["weight"]}")