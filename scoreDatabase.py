import sqlite3
#import Alisha function which continuously calculates the health stat

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