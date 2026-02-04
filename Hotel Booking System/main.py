import sqlite3
import datetime

def FormatDateTime(input):
  format = '%d-%m-%Y'
  return datetime.datetime.strptime(input, format)

database = './Hotel Booking System/database.db'

connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hotel (Booking_ID INTEGER PRIMARY KEY, Start_Date STRING, End_Date STRING, Room_Number INTEGER)")

Start_Date = "1-12-2026"
End_Date = "30-12-2026"

old_data = cursor.execute("SELECT * FROM hotel").fetchall()
#print(old_data)

rooms = 50
current_room = 1
found = False

while current_room <= 50 and not found:
  print("Looping")
  for i in old_data:
    print("Start Date:", i[1])
    print("End Date", i[2])

    print("")

    ## equal
    Equal = (Start_Date == i[1] and End_Date == i[2])
    Start_Between = FormatDateTime(i[1]) <= FormatDateTime(Start_Date) <= FormatDateTime(i[2])
    End_Between = FormatDateTime(i[1]) <= FormatDateTime(End_Date) <= FormatDateTime(i[2])
    Overlap = (FormatDateTime(Start_Date) <= FormatDateTime(i[1]) and FormatDateTime(End_Date) >= FormatDateTime(i[2]))
    Reverse_Overlap = (FormatDateTime(Start_Date) >= FormatDateTime(i[1]) and FormatDateTime(End_Date) <= FormatDateTime(i[2]))

    if not (Equal or Start_Between or End_Between or Overlap or Reverse_Overlap):
      print("Room Found!")
      cursor.execute("INSERT INTO hotel (Start_Date, End_Date, Room_Number) VALUES (?,?,?)", (Start_Date, End_Date, i))
  
  current_room += 1

connection.commit()

