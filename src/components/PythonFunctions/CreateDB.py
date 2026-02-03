import sqlite3 as sql
from BaseFunctions import Databases

if __name__ == "__main__":
  locations = Databases()
  
  ## Checks if the databases actually exist ##
  connection = sql.connect(locations.db_path)
  cursor = connection.cursor()

  ## Create the tables IF THEY DONT ALREADY EXIST ##
  cursor.execute(f"CREATE TABLE IF NOT EXISTS {locations.login} (Account_ID INTEGER PRIMARY KEY AUTOINCREMENT, Username UNIQUE, Password)")
  cursor.execute(f"CREATE TABLE IF NOT EXISTS {locations.bookings} (Booking_ID INTEGER PRIMARY KEY, Type_Of_Bookings STRING ,Account_ID INTEGER REFERENCES Accounts(Account_ID), Date TEXT, Adults INTEGER, Child INTEGER, Membership_Number INTEGER, Username STRING)")
  #cursor.execute(f"CREATE TABLE IF NOT EXISTS {locations.hotel_booking} (Booking_ID INTEGER PRIMARY KEY, Username, start_date, end_date, room_number INTEGER)")#

  print("Connection Established!")