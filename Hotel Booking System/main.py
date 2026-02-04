import sqlite3

database = './Hotel Booking System/database.db'

connection = sqlite3.connect(database)
cursor = connection.cursor()