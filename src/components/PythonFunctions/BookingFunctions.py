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
    locationFound = True
    ## If room is available change this to True
    
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
      for i in range(len(start_list)):
        print(len(start_list))
        print(i)
        print(start_list[i], end_list[i])

        equal = FormatDateTime(start_list[i]) == start_date or FormatDateTime(end_list[i]) == end_date
        start_between = FormatDateTime(start_list[i]) <= start_date <= FormatDateTime(end_list[i])
        end_between = FormatDateTime(start_list[i]) <= end_date <= FormatDateTime(end_list[i])
        overlap = (start_date <= FormatDateTime(start_list[i])) and (end_date >= FormatDateTime(end_list[i]))

        if (overlap or end_between or start_between or equal):
          locationFound = False
          break

      if locationFound:
        AddData(data, RoomNum, start_date, end_date, Account_ID)
        return

    elif locationFound:
      AddData(data, RoomNum, start_date, end_date, Account_ID)
      return

def FormatDateTime(input):
  format = '%Y-%m-%d'
  return datetime.datetime.strptime(input, format)
