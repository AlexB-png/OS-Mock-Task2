from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql

def MakeBooking(username, start, end, booking):
  ## Make a connection to the database ##
  connection, cursor , locations = connect()
  ##
  
  ## Get the account id from Username
  account_id = cursor.execute("SELECT Account_ID FROM Accounts where Username = ?", (username,)).fetchone()
  ##

  ## If there is somehow no account id then return to prevent NonSubscriptable error 
  if not account_id:
    return
  ##

  ## Insert Account_ID , start , end and booking type into bookings database
  cursor.execute("INSERT INTO bookings (Account_ID, Start_date, End_date, Type_Of_Bookings) VALUES (?,?,?,?)", (account_id[0], start, end, booking))
  ##

  connection.commit()
  connection.close()