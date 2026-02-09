import sqlite3
import datetime
from BaseFunctions import Databases, HotelSettings

## Convert String To DateTime ##
def FormatDateTime(input):
  format = '%d-%m-%Y'
  return datetime.datetime.strptime(input, format)
##

## Make the booking into hotel (parameters Starting Date and the End date)
def CreateHotelBooking(Start_Date : string, End_Date : string):
  # src/DataBase.db 
  database = Databases.db_path

  connection = sqlite3.connect(database)
  cursor = connection.cursor()

  rooms = HotelSettings.max_rooms # Typically 50
  current_room = 1
  found = False

  while current_room <= 50 and not found:
    room_num = cursor.execute("SELECT * from Hotel_Bookings WHERE Room_Number = ?",(current_room,)).fetchall()
    if not room_num:
      print("No Bookings Made Yet!")
      cursor.execute("INSERT INTO Hotel_Bookings (Start_Date, End_Date, Room_Number) VALUES (?,?,?)",(Start_Date, End_Date, current_room))
      found = True
      break

    for booking in room_num:
      booking_start_date = booking[1]
      booking_end_date = booking[2]
      booking_room_number = booking[3]
      booking_booking_ID = booking[0]

      Equal = (Start_Date == booking_start_date or End_Date == booking_end_date)
      Start_Between = FormatDateTime(booking_start_date) <= FormatDateTime(Start_Date) <= FormatDateTime(booking_end_date)
      End_Between = FormatDateTime(booking_start_date) <= FormatDateTime(End_Date) <= FormatDateTime(booking_end_date)
      Overlap = (FormatDateTime(Start_Date) <= FormatDateTime(booking_start_date) and FormatDateTime(End_Date) >= FormatDateTime(booking_end_date))
      Reverse_Overlap = (FormatDateTime(Start_Date) >= FormatDateTime(booking_start_date) and FormatDateTime(End_Date) <= FormatDateTime(booking_end_date))

      invalid = Equal or Start_Between or End_Between or Overlap or Reverse_Overlap

      print(invalid)

      if invalid:
        break
      else:
        print("Room Found", current_room)
        cursor.execute("INSERT INTO Hotel_Bookings (Start_Date, End_Date, Room_Number) VALUES (?,?,?)",(Start_Date, End_Date, current_room))
        found = True

    current_room += 1

  connection.commit()
##