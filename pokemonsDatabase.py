import sqlite3
#import Alisha function which continuously calculates the health stat

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


