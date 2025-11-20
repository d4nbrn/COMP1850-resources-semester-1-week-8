"""
Exercise 1.2: Summarise Pokémon Details (Stub)
- Fetch Pokémon data from the PokéAPI.
- Extract specific details: name, types, stats, and image URL.
- Display the extracted details in a readable format.
"""

import httpx

def summarise_pokemon(name):
    """Fetch and summarise Pokémon details."""
    # TODO: Construct the URL using the Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    # TODO: Make a GET request to the URL
    response = httpx.get(url)

    # TODO: Check if the response is successful (status_code == 200)
    if response.status_code == 200:
        # TODO: Parse the JSON response
        data = response.json()

        # TODO: Extract the Pokémon's name
        name = data['name']

        # TODO: Extract the Pokémon's types (list comprehension pulling type_info['type']['name'])
        types = [type_info['type']['name'] for type_info in data['types']]

        # TODO: Extract the Pokémon's base stats
        stats = data['stats']
        base_stats = []
        for items in stats:
            statnumber = items["base_stat"]
            statname = items["stat"]["name"]
            base = [statname,statnumber]
            base_stats.append(base)
        # TODO: Print the details in a readable format
        
        print(f"Name: {name}")
        print(f"Types: {', '.join(types)}")
        print("Base Stats:")
        for stat in base_stats:
            print(f"Stat: {stat[0]} \n Power: {stat[1]}")
    else:
        print(f"Error: Pokémon '{name}' not found!")

# Example usage
summarise_pokemon("squirtle")
