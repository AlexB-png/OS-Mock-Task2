from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql
import json
import datetime

def AddData(Data, RoomNumber, Start_Date, End_Date, ID):
  NewData = Data

  ## Start Date
  Old_Start_Date = NewData[str(RoomNumber)]["start_date"]
  Old_Start_Date.append(Start_Date.date().isoformat())
  NewData[str(RoomNumber)]["start_date"] = Old_Start_Date
  ##

  ## End Date
  Old_End_Date = NewData[str(RoomNumber)]["end_date"]
  Old_End_Date.append(End_Date.date().isoformat())
  NewData[str(RoomNumber)]["end_date"] = Old_End_Date
  ##
  
  ## ID
  Old_ID = NewData[str(RoomNumber)]["user_id"]
  Old_ID.append(ID[0])
  NewData[str(RoomNumber)]["user_id"] = Old_ID
  ##

  with open('src/HotelBookings.json', 'w') as file:
    json.dump(NewData, file, indent=4)

def MakeBooking(username, start, end, booking):
  ## Convert string to datetime for comparing
  format = '%Y-%m-%d'
  start_date = datetime.datetime.strptime(start, format)
  end_date = datetime.datetime.strptime(end, format)
  ##
  
  ## Data is the room booking database
  with open("src/HotelBookings.json", 'r') as file:
    data = json.load(file)
  ##

  for RoomNum in range(1, 51):
    ## If room is available change this to True
    locationFound = False
    ##
    
    ## Store data for the room Number here
    RoomData = data[str(RoomNum)]
    start_list = RoomData['start_date']
    end_list = RoomData['end_date']
    ##

    ## Get User ID 
    connection, cursor , locations = connect()
    Account_ID = cursor.execute(f"SELECT Account_ID FROM {locations.login} WHERE Username = ?", (username,)).fetchone()
    ##

    ## IF Booking start__list and end_list has data in it ##
    if (start_list) and (end_list):
      for start_date_list in start_list:
        for end_date_list in end_list:
          print(start_date_list, end_date_list)
    else:
      AddData(data, RoomNum, start_date, end_date, Account_ID)
      break
