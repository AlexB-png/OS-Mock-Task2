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
  hotel_booking = "Hotel_Bookings"
  bookings = "bookings"

class Colors:
  red = "rgb(255,51,0)"
  green = "#626F47"
  lime = "rgb(153,255,153)"