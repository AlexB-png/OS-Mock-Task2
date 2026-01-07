import sqlite3 as sql

## Makes connection and cursors
def connect():
  locations = Databases()
  
  connection = sql.connect(locations.db_path)
  cursor = connection.cursor()

  return connection , cursor , locations
##

class Databases:
  ## Place DataBase Locations in here ##
  db_path = "src/DataBase.db"

  login = "Accounts"
  bank = "Bank_Details"

class Colors:
  red = rgb