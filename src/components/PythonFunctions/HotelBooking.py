import sqlite3
import datetime
from .BaseFunctions import Databases, HotelSettings

## Convert String To DateTime ##
def FormatDateTime(input):
  format = '%Y-%m-%d'
  return datetime.datetime.strptime(input, format)
##

## Make the booking into hotel (parameters Starting Date and the End date)
def CreateHotelBooking(Start_Date : str, End_Date : str, Account_Name : str, Guests : int, Singles : int, Doubles : int):
  # src/DataBase.db 
  database = Databases.db_path

  connection = sqlite3.connect(database)
  cursor = connection.cursor()

  rooms = HotelSettings.max_rooms # Typically 50 # Change this in BaseFunctions.py
  current_room = 1
  found = False

  Account_ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (Account_Name,)).fetchall()[0][0]
  print(Account_ID)

  while current_room <= rooms and not found:
    # Get data for a specific room number
    room_num = cursor.execute("SELECT * from Hotel_Bookings WHERE Room_Number = ?",(current_room,)).fetchall()
    
    # If the room number is empty then break the loop and add booking to database
    if not room_num:
      print("No Bookings Made Yet!")
      cursor.execute("INSERT INTO Hotel_Bookings (Start_Date, End_Date, Room_Number, Account_ID, Guests, Singles, Doubles) VALUES (?,?,?,?,?,?,?)",(Start_Date, End_Date, current_room, Account_ID, Guests, Singles, Doubles))
      found = True
      connection.commit()
      return "Successfully Made Booking"

    # Iterate over the data for the room number to check if there is a booking already
    for booking in room_num:
      booking_start_date = booking[1]
      booking_end_date = booking[2]
      booking_room_number = booking[3]
      booking_booking_ID = booking[0]

      # Check if start date or end date is equal
      Equal = (Start_Date == booking_start_date or End_Date == booking_end_date)
      
      # Check if the selected start falls between the already booked rooms
      Start_Between = FormatDateTime(booking_start_date) <= FormatDateTime(Start_Date) <= FormatDateTime(booking_end_date)
      
      # Check if the selected end date falls between the already booked dates
      End_Between = FormatDateTime(booking_start_date) <= FormatDateTime(End_Date) <= FormatDateTime(booking_end_date)
      
      # Check if the start date is before booked start and end date is after booked end
      Overlap = (FormatDateTime(Start_Date) <= FormatDateTime(booking_start_date) and FormatDateTime(End_Date) >= FormatDateTime(booking_end_date))
      
      # Check if the start date is after booked start and end date is before booked end
      Reverse_Overlap = (FormatDateTime(Start_Date) >= FormatDateTime(booking_start_date) and FormatDateTime(End_Date) <= FormatDateTime(booking_end_date))

      # One variable for all
      invalid = Equal or Start_Between or End_Between or Overlap or Reverse_Overlap

      # debug
      print(invalid)

      # If the dates are invalid then dont repeat loop for this room number and set found to false
      if invalid:
        found = False
        break
      else:
        found = True
    if found:
      print("Room Found", current_room)
      cursor.execute("""INSERT INTO Hotel_Bookings
                      (Start_Date, End_Date, Room_Number) VALUES (?,?,?)"""
                      ,(Start_Date, End_Date, current_room))
      connection.commit()
      return "Successfully Made Booking"

    # Iterate up the room that is being checked
    current_room += 1
  
  return "No Rooms Available"
##