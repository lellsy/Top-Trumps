import requests
import random
import sqlite3

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

def insert_data_pokemons(user, round, pokemon_name, initial_hp, pokemon_id, height, weight):
 conn = sqlite3.connect('pokemons.db') #database connection
 c = conn.cursor() #cursor creates table, inserts data etc
 dictionary = {"user_name": user, "round": round,"pokemon_name": pokemon_name,"pokemon_id": pokemon_id,"height": height,"weight": weight} 

 c.execute("INSERT OR REPLACE INTO pokemons (user, round, pokemon_name, pokemon_id, height, weight) VALUES (:user_name, :round, :pokemon_name, :pokemon_id, :height, :weight)", dictionary) #adding data to table
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







#calculates the hp based on average of all 5 pokemon of the chosen stat
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)