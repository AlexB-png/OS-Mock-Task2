import sqlite3

database = './Hotel Booking System/database.db'

connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute("INSERT INTO hotel (Start_Date, End_Date, Room_Number) VALUES (?,?,?)",("15-12-2026", "16-12-2026", 2))

connection.commit()