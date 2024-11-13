import requests
import random
import sqlite3


round = 1

#Giorgia's code start
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


def insert_data_scores(player_hp, computer_hp):
 #import health stat data from Alisha 
 conn = sqlite3.connect('scores.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc
 c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_id ON scores(id_user);")
 info_player = {'id_user':1,'user':'player','health_stat':player_hp} #get health variable from Alisha 
 info_computer = {'id_user':2,'user':'computer','health_stat':computer_hp} #get health variable from Alisha 

 c.execute("INSERT OR REPLACE INTO scores (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_player) #adding data to table
 c.execute("INSERT OR REPLACE INTO scores (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_computer) #adding data to table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened 

def delete_data_scores():
  conn = sqlite3.connect('scores.db') #database connection
  c = conn.cursor() #cursor creates table, inserts data etc
  c.execute("DELETE FROM scores") #deleting the data
  conn.commit() #by committing we are saving our changes to the database
  conn.close() #closing the connection previously opened 


def create_table_pokemons():
 conn = sqlite3.connect('pokemons.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc

 c.execute("""CREATE TABLE IF NOT EXISTS pokemons (  
          user TEXT,
          round INTEGER,
          pokemon_name TEXT,
          pokemon_id INTEGER, 
          height INTEGER,
          weight INTEGER
          )""") #create table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened

def insert_data_pokemons(user, round, pokemon_name, pokemon_id, height, weight):
 conn = sqlite3.connect('pokemons.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc
 dictionary = {"user_name": user, "round": round,"pokemon_name": pokemon_name,"pokemon_id": pokemon_id,"height": height,"weight": weight} 

 c.execute("INSERT OR REPLACE INTO pokemons (user, round, pokemon_name, pokemon_id, height, weight) VALUES (:user_name, :round, :pokemon_name, :pokemon_id, :height, :weight)", dictionary) #adding data to table
 conn.commit() #by committing we are saving our changes to the database
 conn.close() #closing the connection previously opened 

def delete_data_pokemons():
  conn = sqlite3.connect('pokemons.db') #database connection
  c = conn.cursor() #cursor creates table, inserts data etc
  c.execute("DELETE FROM pokemons") #deleting the data
  conn.commit() #by committing we are saving our changes to the database
  conn.close() #closing the connection previously opened 




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
   pokemon_name = pokemon_player['name']
   pokemon_id = pokemon_player['id']
   height = pokemon_player['height']
   weight = pokemon_player['weight']
   create_table_pokemons()
   insert_data_pokemons(user, round, pokemon_name, pokemon_id, height, weight)
   pokemon_dict_player = {pokemon_name:{ "id": pokemon_id,"height": height,"weight": weight}}
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
   user = "computer"
   pokemon_name = pokemon_computer['name']
   pokemon_id = pokemon_computer['id']
   height = pokemon_computer['height'] 
   weight = pokemon_computer['weight']
   create_table_pokemons()
   insert_data_pokemons(user, round, pokemon_name, pokemon_id, height, weight)
   pokemon_dict_computer = {pokemon_name:{"id": pokemon_id,"height": height,"weight": weight}}
   selected_pokemons.update(pokemon_dict_computer)
  except requests.ConnectionError:
   print("An error has occured!")
 return selected_pokemons

#Giorgia's code end

#Chisom's code start
 # Get player and computer Pokémon data
# player_pokemons = player_data(round)
# computer_pokemons = computer_data(round)

# Display data for comparison
# print("Welcome to Pokémon Top Trumps!\n")
# print("Player's Pokémon:")
# print(player_pokemons)
# print("\nComputer's Pokémon:")
# print(computer_pokemons)


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

#calculates the hp based on average of all 5 pokemon of the chosen stat
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)


#Alisha Code Starts
#def battle(player_pokemons, computer_pokemons, chosen_stat):
    #"""Main game loop, continues rounds until a winner is decided."""
    #player_hp = calculate_initial_hp(player_pokemons, chosen_stat)
    #computer_hp = calculate_initial_hp(computer_pokemons, chosen_stat)
    
    #print("\nStarting battle!")
    #print(f"Player HP: {player_hp}, Computer HP: {computer_hp}")
    #print(f"Chosen stat for the game: {chosen_stat}\n")
    
    #while player_team and computer_team and player_hp > 0 and computer_hp > 0:
       # player_hp, computer_hp = round(player_team, computer_team, player_hp, computer_hp, chosen_stat)
       # print(f"Current HP -> Player: {player_hp}, Computer: {computer_hp}")
#Alisha Code Ends


def battle(player_pokemon, computer_pokemon, total_stat, computer_hp, player_hp):
    """Compares the chosen stat of two Pokémon to determine the winner."""
    player_stat = player_pokemon[total_stat]
    computer_stat = computer_pokemon[total_stat]

    player_hp = calculate_initial_hp(player_pokemons, stat_choice)
    computer_hp = calculate_initial_hp(computer_pokemons, stat_choice)
    print(f"\nBattle! Player's {player_hp} vs Computer's {computer_hp}")
    

    player_stat = player_pokemon[total_stat]
    computer_stat = computer_pokemon[total_stat]

    if player_stat > computer_stat:
        # pif the player wins this round
        damage = player_stat - computer_stat
        computer_hp -= damage
        print(f"Player wins this round! Computer loses {damage} HP.")
        player_pokemon.append(player_pokemon)  
        # winner's pokemon goes back to team

    elif computer_stat > player_stat:
        # computer wins this round
        damage = computer_stat - player_stat
        player_hp -= damage
        print(f"Computer wins this round! Player loses {damage} HP.")
        computer_pokemon.append(computer_pokemon)  
        # winner's pokemon goes back to team

    else:
        # if its a tie they both lose
        print("It's a tie! Both Pokémon are discarded.")

    return player_hp, computer_hp

    #if player_stat > computer_stat:
       # print("Player's Pokémon wins!")
       # return "player"
    #elif computer_stat > player_stat:
        #print("Computer's Pokémon wins!")
        #return "computer"
    #else:
       #print("It's a tie!")
    #return "tie"


def game_loop():
    # Initial setup
    global player_pokemons
    global computer_pokemons

    player_pokemons = player_data(round)
    computer_pokemons = computer_data(round)

    # Player selects the stat to compete on
    print("Choose a stat for battle (id, height, weight):")
    global stat_choice
    stat_choice = input().strip().lower()
    if stat_choice not in ["id", "height", "weight"]:
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


def calc_round(value):
   if not player_pokemons or not computer_pokemons:
      value += 1
   return value

def main():
    global round 
    while True:
        game_loop()
        round = calc_round(round)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            delete_data_scores()
            delete_data_pokemons()
            break

# Start the game
main()
#Chisom's code ends