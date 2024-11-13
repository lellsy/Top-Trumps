import random 
import requests
from pokemonsDatabase import create_table_pokemons, insert_data_pokemons
#from pokemon import calculate_initial_hp

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





print(player_data(round))
print(computer_data(round))



