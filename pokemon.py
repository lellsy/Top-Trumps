import requests
import random
import sqlite3 

round = 1 
#score database code
def create_table_scores():

 conn = sqlite3.connect('scores.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc

 c.execute("""CREATE TABLE IF NOT EXISTS scores( 
          id_user INTEGER, 
          user TEXT,
          health_stat INTEGER
          )""") #create table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened


def insert_data_scores():
 #import health stat data from Alisha 
 conn = sqlite3.connect('scores.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc
 c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_id ON scores(id_user);")
 info_player = {'id_user':1,'user':'player','health_stat':65} #get health variable from Alisha 
 info_computer = {'id_user':2,'user':'computer','health_stat':75} #get health variable from Alisha 

 c.execute("INSERT OR REPLACE INTO scores (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_player) #adding data to table
 c.execute("INSERT OR REPLACE INTO scores (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_computer) #adding data to table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened 


#pokemons database
def create_table_pokemons():

 conn = sqlite3.connect('pokemons.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc

 c.execute("""CREATE TABLE IF NOT EXISTS pokemons (  
          user TEXT,
          round INTEGER,
          pokemon_name TEXT,
          initial_hp INTEGER, 
          pokemon_id INTEGER, 
          height INTEGER,
          weight INTEGER
          )""") #create table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened

def insert_data_pokemons(user, round, pokemon_name, initial_hp, pokemon_id, height, weight):
 conn = sqlite3.connect('pokemons.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc
 dictionary = {"user_name": user, "round": round,"pokemon_name": pokemon_name,"initial_hp": initial_hp,"pokemon_id": pokemon_id,"height": height,"weight": weight} 

 c.execute("INSERT OR REPLACE INTO pokemons (user, round, pokemon_name, initial_hp, pokemon_id, height, weight) VALUES (:user_name, :round, :pokemon_name, :initial_hp, :pokemon_id, :height, :weight)", dictionary) #adding data to table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened 


#Giorgia: getting the pokemons from the api and storing them in the api database
#there is a a repetition with Chisom code 
round = 1

def player_data(round):
 no_pokemons = 5 #number of pokemons that will be played
 selected_pokemons = {}
 for i in range(no_pokemons):
  try:
   random_player = random.randint(1, 151)
   url_player = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_player)
   response_player = requests.get(url_player)
   pokemon_player = response_player.json()
   user = "player"
   initial_hp = 76 #calculate_initial_hp() health stat obained from calculate_initial_hp function
   pokemon_name = pokemon_player['name']
   pokemon_id = pokemon_player['id']
   height = pokemon_player['height']
   weight = pokemon_player['weight']
   create_table_pokemons()
   insert_data_pokemons(user, round, pokemon_name, initial_hp, pokemon_id, height, weight)
   pokemon_dict_player = {pokemon_name:{"health stat": initial_hp, "id": pokemon_id,"height": height,"weight": weight}}
   selected_pokemons.update(pokemon_dict_player)
  except requests.ConnectionError:
   print("An error has occured!")
   
 return selected_pokemons
 

def computer_data(round):
 no_pokemons = 5 #number of pokemons that will be played
 selected_pokemons = {}
 for i in range(no_pokemons):
  try:
   random_computer = random.randint(1, 151)
   url_player = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_computer)
   response_computer = requests.get(url_player)
   pokemon_computer = response_computer.json()
   initial_hp = 56#calculate_initial_hp() health stat obained from calculate_initial_hp function
   user = "computer"
   pokemon_name = pokemon_computer['name']
   pokemon_id = pokemon_computer['id']
   height = pokemon_computer['height'] 
   weight = pokemon_computer['weight']
   create_table_pokemons()
   insert_data_pokemons(user, round, pokemon_name, initial_hp, pokemon_id, height, weight)
   pokemon_dict_computer = {pokemon_name:{"health stat": initial_hp, "id": pokemon_id,"height": height,"weight": weight}}
   selected_pokemons.update(pokemon_dict_computer)
  except requests.ConnectionError:
   print("An error has occured!")
 
 return selected_pokemons



#set up the api to retrieve pokemon data
def get_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()


#SQL Database. returning names +stats - Giorgia


#calculates the hp based on average of all 5 pokemon of the chosen stat - Alisha
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)


#prints the whole team and lets player pick their stats - Chisom

def get_random_pokemon_team(size=5):
    """
    Generates a team of random Pokémon
    """
    pokemon_ids = random.sample(range(1, 152), size)  # Random Pokémon IDs from 1 to 151
    team = [get_pokemon(pokemon_id) for pokemon_id in pokemon_ids]
    return team

def display_pokemon(pokemon):
    """Displays Pokémon details."""
    print(f"\nPokemon: {pokemon['name']}")
    print(f"Type: {pokemon['type'].capitalize()}")
    print(f"ID: {pokemon['id']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")

def can_play_pokemon(pokemon, active_pokemon, stat_choice):
    """
    Check if a Pokémon can be played (Uno-style rules)
    Returns: (bool, str) - Can be played and reason why
    """
    if not active_pokemon:  # First turn - can play anything
        return True, "First turn"

    # Can play if same type (like matching color in Uno)
    if pokemon['type'] == active_pokemon['type']:
        return True, "Matching type!"

    # Can play if stat is equal or higher (like numbers in Uno)
    if pokemon[stat_choice] >= active_pokemon[stat_choice]:
        return True, "Equal or higher stat!"
    else:
        return False, "Cannot play this Pokémon"

def main_game():
    print("\nWelcome to Pokémon Top Trumps - Uno Style!")
    print("Choose the stat that will be used for all battles:")
    print("1. ID")
    print("2. Height")
    print("3. Weight")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            stat_choice = ['id', 'height', 'weight'][int(choice) - 1]
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
   
#Game play (player picks pokemon to fight) - Chisom

print("\nGenerating Pokemon teams...")
    player_team = get_random_pokemon_team()
    computer_team = get_random_pokemon_team()

    print(f"\nYou've been given {len(player_team)} Pokémon!")
    active_pokemon = None  # This is the currently winning Pokémon on the table



           
            


#subtracts the damage off of the total hp - Alisha
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


#repeats cycle - Chisom

#Assigning teams - Giorgia

#player picks stat - Chisom

# Start the battle
battle(player_team, computer_team, chosen_stat)

round +=1
