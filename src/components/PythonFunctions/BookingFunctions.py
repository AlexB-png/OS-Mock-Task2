from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql
import json
import datetime

def MakeBooking(username, start, end, booking):
  ## Convert string to datetime for comparing
  format = '%Y-%m-%d'
  start_date = datetime.datetime.strptime(start, format)
  end_date = datetime.datetime.strptime(end, format)
  ##

  ## Test
  test_start = datetime.datetime.strptime("2026-01-01", format)
  test_end = datetime.datetime.strptime("2026-01-02", format)
  ##

  if test_start <= start_date <= test_end or test_start <= end_date <= test_end or (start_date <= test_start and end_date >= test_end):
    print("Within dates!")

  #print(start_date, end_date)
  
  ## Make a connection to the database ##
  connection, cursor , locations = connect()
  ##
  
  ## Get the account id from Username
  account_id = cursor.execute("SELECT Account_ID FROM Accounts where Username = ?", (username,)).fetchone()
  ##

  ## If there is somehow no account id then return to prevent NonSubscriptable error 
  if not account_id:
    print("No ID")
    return
  ##

  with open("src/HotelBookings.json", 'r') as file:
    data = json.load(file)

  for RoomNum in range(1,51):
    room = data[str(RoomNum)]
    
    start_date = "START"
    end_date = "END"
    user_ID = "TEST"

    start_list = room["start_date"]
    end_list = room["end_date"]

    if start_list and end_list:
      for start in start_list:
        for end in end_list:
          print(start, end)
    else:
      print(room, start_list, end_list)

    #print(RoomNum)
    #print("Start Date:", start_list)
    #print("End Date", end_list)

    if not start_list and not end_list:
      break

  ## Insert Account_ID , start , end and booking type into bookings database
  #cursor.execute("INSERT INTO bookings (Account_ID, Start_date, End_date, Type_Of_Bookings) VALUES (?,?,?,?)", (account_id[0], start, end, booking))
  ##

  connection.commit()
  connection.close()