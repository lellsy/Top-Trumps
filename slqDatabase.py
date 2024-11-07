import sqlite3

conn = sqlite3.connect('pokemons.db') #database connection

c = conn.cursor() #cursor creates table, inserts data etc

c.execute("""CREATE TABLE IF NOT EXISTS pokemons ( 
          id_user INTEGER, 
          user TEXT,
          health_stat INTEGER
          )""") #create table

c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_id ON pokemons(id_user);")
info_player = {'id_user':1,'user':'player','health_stat':65}
info_computer = {'id_user':2,'user':'computer','health_stat':75}

c.execute("INSERT OR REPLACE INTO pokemons (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_player) #adding data to table
c.execute("INSERT OR REPLACE INTO pokemons (id_user, user, health_stat) VALUES (:id_user, :user, :health_stat)", info_computer) #adding data to table




#c.executemany("INSERT INTO pokemons VALUES(?, ?, ?, ?, ?, ?, ?)")#adding data to table


conn.commit() #by committing we are saving our changes to the database
conn.close() #closing the connection previously opened

