import random
import requests
from pprint import pprint

def get_pokemon_data(no_pokemons=5):
    """Fetches data for the given number of random Pokémon."""
    selected_pokemons = {}
    for i in range(no_pokemons):
        pokemon_id = random.randint(1, 151)
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure the request was successful
            pokemon_data = response.json()
            # Extract health stat and other info
            stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
            selected_pokemons[pokemon_data['name']] = {
                "health stat": stats.get("hp"),
                "id": pokemon_data['id'],
                "height": pokemon_data['height'],
                "weight": pokemon_data['weight'],
            }
        except requests.RequestException as e:
            print(f"Error fetching data for Pokémon ID {pokemon_id}: {e}")
    return selected_pokemons

# Get player and computer Pokémon data
player_pokemons = get_pokemon_data()
computer_pokemons = get_pokemon_data()

# Display data for comparison
print("Welcome to Pokémon Top Trumps!\n")
print("Player's Pokémon:")
pprint(player_pokemons)
print("\nComputer's Pokémon:")
pprint(computer_pokemons)


def player_select_pokemon(pokemon_list):
    """Allows the player to select a Pokémon from their list."""
    print("Your Pokémon:")
    for i, (name, stats) in enumerate(pokemon_list.items(), start=1):
        print(f"{i}. {name} - Stats: {stats}")
    choice = int(input("Choose your Pokémon by entering the number: ")) - 1
    pokemon_name = list(pokemon_list.keys())[choice]
    return pokemon_name, pokemon_list[pokemon_name]


def computer_select_pokemon(pokemon_list):
    """Randomly selects a Pokémon for the computer."""
    pokemon_name = random.choice(list(pokemon_list.keys()))
    return pokemon_name, pokemon_list[pokemon_name]


def battle(player_pokemon, computer_pokemon, stat_choice):
    """Compares the chosen stat of two Pokémon to determine the winner."""
    player_stat = player_pokemon[stat_choice]
    computer_stat = computer_pokemon[stat_choice]
    print(f"\nBattle! Player's {player_stat} vs Computer's {computer_stat}")
    if player_stat > computer_stat:
        print("Player's Pokémon wins!")
        return "player"
    elif computer_stat > player_stat:
        print("Computer's Pokémon wins!")
        return "computer"
    else:
        print("It's a tie!")
        return "tie"


def game_loop():
    # Initial setup
    player_pokemons = get_pokemon_data()
    computer_pokemons = get_pokemon_data()

    # Player selects the stat to compete on
    print("Choose a stat for battle (hp, id, height, weight):")
    stat_choice = input().strip().lower()
    if stat_choice not in ["hp", "id", "height", "weight"]:
        print("Invalid stat choice. Please choose again.")
        return

    # Game loop
    while player_pokemons and computer_pokemons:
        # Player chooses a Pokémon
        player_pokemon_name, player_pokemon_stats = player_select_pokemon(player_pokemons)

        # Computer randomly chooses a Pokémon
        computer_pokemon_name, computer_pokemon_stats = computer_select_pokemon(computer_pokemons)

        # Display chosen Pokémon
        print(f"\nPlayer's chosen Pokémon: {player_pokemon_name} - {player_pokemon_stats}")
        print(f"Computer's chosen Pokémon: {computer_pokemon_name} - {computer_pokemon_stats}")

        # Battle
        winner = battle(player_pokemon_stats, computer_pokemon_stats, stat_choice)

        # Remove the losing Pokémon
        if winner == "player":
            del computer_pokemons[computer_pokemon_name]
        elif winner == "computer":
            del player_pokemons[player_pokemon_name]
        else:  # In case of a tie, both Pokémon are removed
            del player_pokemons[player_pokemon_name]
            del computer_pokemons[computer_pokemon_name]

        # Check if game is over
        if not player_pokemons:
            print("\nComputer wins the game!")
            break
        elif not computer_pokemons:
            print("\nPlayer wins the game!")
            break


def main():
    while True:
        game_loop()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
main()