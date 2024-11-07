import random
import requests


# Fgets pokemon stats and names from api
def get_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()  # Get the Pokémon's name and capitalise it
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        return name, stats
    else:
        print(f"Error fetching data for Pokémon ID {pokemon_id}")
        return None, None



def calculate_health(stats):
    # calculates the average number from stats and sets that as the health
    stat_values = [value for stat, value in stats.items() if stat != 'hp']
    average_stat_value = sum(stat_values) / len(stat_values)

    # sets health to the average (rounds it up to whole number)
    health = round(average_stat_value)
    return health


# compares the health stats between the two
def compare_pokemon_health(pokemon_id_1, pokemon_id_2):
    name_1, stats_1 = get_pokemon_info(pokemon_id_1)
    name_2, stats_2 = get_pokemon_info(pokemon_id_2)

    if not stats_1 or not stats_2:
        print("Error retrieving stats, cannot compare.")
        return

    health_1 = calculate_health(stats_1)
    health_2 = calculate_health(stats_2)

    print(f"Health for {name_1} (ID {pokemon_id_1}): {health_1}")
    print(f"Health for {name_2} (ID {pokemon_id_2}): {health_2}")

    # compares the health points
    if health_1 > health_2:
        print(f"{name_1} has higher health points ({health_1} vs {health_2})")
    elif health_1 < health_2:
        print(f"{name_2} has higher health points ({health_2} vs {health_1})")
    else:
        print(f"Both have equal health points ({health_1} vs {health_2})")


# Randomly selects 2 pokemon
def main():

    pokemon_id_1 = random.randint(1, 151)
    pokemon_id_2 = random.randint(1, 151)

    # Makes sure its not the same
    while pokemon_id_1 == pokemon_id_2:
        pokemon_id_2 = random.randint(1, 151)

    print(f"Comparing health of Pokémon with IDs {pokemon_id_1} and {pokemon_id_2}...\n")
    compare_pokemon_health(pokemon_id_1, pokemon_id_2)


# runs the main function
if __name__ == "__main__":
    main()