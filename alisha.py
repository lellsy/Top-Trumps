import requests
import random
from scoreDatabase import create_table_scores, insert_data_scores

#sets up the api to get 5 random pokemon
def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

 #returns their names and stats   
    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()
        hp = next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp")
        height = data["height"]
        weight = data["weight"]
        return {"name": name, "hp": hp, "height": height, "weight": weight, "id": pokemon_id}
    else:
        return None

#assigns 5 random pokemon to form player and opponents teams
def assign_teams(num_pokemon=5):
    player_team = []
    computer_team = []
    
    for _ in range(num_pokemon):
        player_pokemon = get_random_pokemon()
        computer_pokemon = get_random_pokemon()
        
        if player_pokemon:
            player_team.append(player_pokemon)
        if computer_pokemon:
            computer_team.append(computer_pokemon)
    
    return player_team, computer_team

#calculates the hp based on average of all 5 pokemon of the chosen stat
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)

#prints whole team and lets player choose a stat
def choose_player_pokemon(player_team):
    print("\nYour team:")
    for pokemon in player_team:
        print(f"{pokemon['name']} - ID: {pokemon['id']}, Height: {pokemon['height']}, Weight: {pokemon['weight']}")
    
    chosen_name = input("Choose a Pokémon from your team by name: ").capitalize()
    
    # finds and returns the chosen pokemon
    for pokemon in player_team:
        if pokemon["name"] == chosen_name:
            return player_team.pop(player_team.index(pokemon))
    
    print("Invalid choice. Please choose a Pokémon by entering the exact name.")
    return choose_player_pokemon(player_team)

#rounds start
def play_round(player_team, computer_team, player_hp, computer_hp, chosen_stat):
  
    # player picks a pokemon from their team
    player_pokemon = choose_player_pokemon(player_team)
    # computer automatically picks its first pokemon
    computer_pokemon = computer_team.pop(0)
    
    player_stat = player_pokemon[chosen_stat]
    computer_stat = computer_pokemon[chosen_stat]
    
    print(f"\nPlayer's {player_pokemon['name']} (Stat {chosen_stat}: {player_stat}) vs "
          f"Computer's {computer_pokemon['name']} (Stat {chosen_stat}: {computer_stat})")
    
    if player_stat > computer_stat:
        # pif the player wins this round
        damage = player_stat - computer_stat
        computer_hp -= damage
        print(f"Player wins this round! Computer loses {damage} HP.")
        player_team.append(player_pokemon)  
        # winner's pokemon goes back to team

    elif computer_stat > player_stat:
        # computer wins this round
        damage = computer_stat - player_stat
        player_hp -= damage
        print(f"Computer wins this round! Player loses {damage} HP.")
        computer_team.append(computer_pokemon)  
        # winner's pokemon goes back to team

    else:
        # if its a tie they both lose
        print("It's a tie! Both Pokémon are discarded.")

    return player_hp, computer_hp

    insert_data_scores()
    create_table_scores(player_hp, computer_hp)

#loops this sequence
def battle(player_team, computer_team, chosen_stat):
    """Main game loop, continues rounds until a winner is decided."""
    player_hp = calculate_initial_hp(player_team, chosen_stat)
    computer_hp = calculate_initial_hp(computer_team, chosen_stat)
    
    print("\nStarting battle!")
    print(f"Player HP: {player_hp}, Computer HP: {computer_hp}")
    print(f"Chosen stat for the game: {chosen_stat}\n")
    
    while player_team and computer_team and player_hp > 0 and computer_hp > 0:
        player_hp, computer_hp = play_round(player_team, computer_team, player_hp, computer_hp, chosen_stat)
        print(f"Current HP -> Player: {player_hp}, Computer: {computer_hp}")
    
    # prints the winner
    if player_hp <= 0 or not player_team:
        print("Computer wins the battle!")
    elif computer_hp <= 0 or not computer_team:
        print("Player wins the battle!")
    else:
        print("It's a tie!")

# assigns teams
player_team, computer_team = assign_teams()
print("Player's Team:", [p['name'] for p in player_team])
print("Computer's Team:", [c['name'] for c in computer_team])

# Player selects a stat to battle with
valid_stats = ["id", "height", "weight"]
chosen_stat = input("Choose a stat to battle with (id, height, weight): ").lower()
while chosen_stat not in valid_stats:
    chosen_stat = input("Invalid choice. Please choose either 'id', 'height', or 'weight': ").lower()

# Start the battle
battle(player_team, computer_team, chosen_stat)
