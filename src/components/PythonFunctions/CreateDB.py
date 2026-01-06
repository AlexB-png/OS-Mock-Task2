import sqlite3 as sql
from BaseFunctions import Databases

if __name__ == "__main__":
  locations = Databases()
  
  ## Checks if the databases actually exist ##
  connection = sql.connect(locations.db_path)
  cursor = connection.cursor()

  ## Create the tables IF THEY DONT ALREADY EXIST ##
  cursor.execute(f"CREATE TABLE IF NOT EXISTS {locations.login} (Account_ID INTEGER PRIMARY KEY AUTOINCREMENT, Username UNIQUE, Password)")

  print("Connection Established!")