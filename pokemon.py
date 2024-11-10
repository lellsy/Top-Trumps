import requests
import random

#sets up the api to get 5 random pokemon
def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)


#SQL Database. returning names +stats - Giorgia


#calculates the hp based on average of all 5 pokemon of the chosen stat - Alisha
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)

#prints the whole team and lets player pick their stats - Chisom

#Game play (player picks pokemon to fight) - Chisom

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
