from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql

def DeleteAccount(username):
  connection, cursor , locations = connect()

  try:
    userId = cursor.execute("SELECT Account_ID FROM Accounts WHERE Username = ?", (username,)).fetchone()[0]
  except:
    return {"status": False , "message" : "Failed! Error 404 : Login Details Not Found"}
  cursor.execute("DELETE FROM Accounts WHERE Account_ID = ?", (userId,))

  connection.commit()
  connection.close()

  return {"status": True , "message" : "Success!"}