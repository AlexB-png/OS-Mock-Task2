from .BaseFunctions import Databases, connect, Colors

def Promote(user_ID : int, option : bool):
  connection, cursor , locations = connect()

  if option:
    cursor.execute("UPDATE Accounts Set Admin = 1 WHERE Account_ID = ?", (user_ID,))
  else:
    cursor.execute("UPDATE Accounts Set Admin = 0 WHERE Account_ID = ?", (user_ID,))
  
  connection.commit()
  connection.close()