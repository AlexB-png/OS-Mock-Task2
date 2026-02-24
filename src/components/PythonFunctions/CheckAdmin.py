from .BaseFunctions import Databases, connect, Colors

def CheckAdmin(username):
  connection, cursor , locations = connect()

  user_ID = cursor.execute("SELECT Account_ID FROM Accounts WHERE Username = ? AND Admin = 1", (username,)).fetchone()
  if not user_ID:
    return False
  else:
    return True