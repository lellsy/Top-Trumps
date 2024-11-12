import requests
import random
from scoreDatabase import create_table_scores, insert_data_scores








#calculates the hp based on average of all 5 pokemon of the chosen stat
def calculate_initial_hp(team, chosen_stat):
    total_stat = sum(pokemon[chosen_stat] for pokemon in team)
    return total_stat // len(team)