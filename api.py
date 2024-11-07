import random 
import requests
from pprint import pprint

#random_player = random.randint(1, 151)
random_computer = random.randint(1, 151)


def player_data():
 no_pokemons = 5 #number of pokemons that will be played
 selected_pokemons = {}
 for i in range(no_pokemons):
  random_player = random.randint(1, 151)
  url_player = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_player)
  response_player = requests.get(url_player)
  pokemon_player = response_player.json()
  stats = pokemon_player['stats']
  for stat in stats:
   if stat['stat']['name'] == 'hp':
    hp = stat['base_stat']
  selected_pokemons.update({pokemon_player['name']:{"health stat": hp, "id": pokemon_player['id'],"height": pokemon_player['height'],"weight": pokemon_player['weight']}})
 return selected_pokemons
 

def computer_data():
 no_pokemons = 5 #number of pokemons that will be played
 selected_pokemons = {}
 for i in range(no_pokemons):
  random_computer = random.randint(1, 151)
  url_player = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_computer)
  response_computer = requests.get(url_player)
  pokemon_computer = response_computer.json()
  stats = pokemon_computer['stats']
  for stat in stats:
   if stat['stat']['name'] == 'hp':
    hp = stat['base_stat']
  selected_pokemons.update({pokemon_computer['name']:{"health stat": hp, "id": pokemon_computer['id'],"height": pokemon_computer['height'],"weight": pokemon_computer['weight']}})
 return selected_pokemons





#print(player_data())
#print(computer_data())



