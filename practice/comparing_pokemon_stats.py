import random
import requests


# Function to get the total number of Pokémon from the API
def get_total_pokemon_count():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['count']  # This gives the total number of Pokémon
    else:
        print("Error fetching total Pokémon count")
        return None


# Function to get a Pokémon's stats based on its ID
def get_pokemon_stats(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        return stats
    else:
        print(f"Error fetching data for Pokémon ID {pokemon_id}")
        return None


# Function to compare the stats of two randomly selected Pokémon
def compare_pokemon(pokemon_id_1, pokemon_id_2):
    stats_1 = get_pokemon_stats(pokemon_id_1)
    stats_2 = get_pokemon_stats(pokemon_id_2)

    if not stats_1 or not stats_2:
        print("Error retrieving stats, cannot compare.")
        return

    print(f"Stats for Pokémon with ID {pokemon_id_1}:")
    for stat, value in stats_1.items():
        print(f"{stat.capitalize()}: {value}")

    print(f"\nStats for Pokémon with ID {pokemon_id_2}:")
    for stat, value in stats_2.items():
        print(f"{stat.capitalize()}: {value}")

    print("\nComparison:")
    for stat in stats_1:
        stat_1_value = stats_1[stat]
        stat_2_value = stats_2[stat]
        if stat_1_value > stat_2_value:
            print(f"ID {pokemon_id_1} has a higher {stat.capitalize()} ({stat_1_value} vs {stat_2_value})")
        elif stat_1_value < stat_2_value:
            print(f"ID {pokemon_id_2} has a higher {stat.capitalize()} ({stat_2_value} vs {stat_1_value})")
        else:
            print(f"Both have equal {stat.capitalize()} ({stat_1_value} vs {stat_2_value})")


# Main function to select two random Pokémon based on their IDs and compare their stats
def main():
    total_pokemon_count = get_total_pokemon_count()

    if total_pokemon_count is None:
        return

    # Randomly select two different Pokémon IDs
    pokemon_id_1 = random.randint(1, total_pokemon_count)
    pokemon_id_2 = random.randint(1, total_pokemon_count)

    # Make sure the IDs are not the same
    while pokemon_id_1 == pokemon_id_2:
        pokemon_id_2 = random.randint(1, total_pokemon_count)

    print(f"Comparing stats of Pokémon with IDs {pokemon_id_1} and {pokemon_id_2}...\n")
    compare_pokemon(pokemon_id_1, pokemon_id_2)


# Run the main function
if __name__ == "__main__":
    main()