from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql

def MakeBooking(username):
  connection, cursor , locations = connect()
  bookings_db = locations.bookings

  account_id = cursor.execute("SELECT Account_ID FROM Accounts where Username = ?", (username,)).fetchone()[0]
  print(account_id)
  cursor.execute("INSERT INTO bookings (Account_ID, Start_date, End_date) VALUES (?,?,?)", (account_id, "123", "456"))

  connection.commit()
  connection.close()

MakeBooking("12345678")