from .BaseFunctions import Databases, connect, Colors

def LoyaltySystem(username):
  connection, cursor , locations = connect()

  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]
  
  currentLoyalty += 1

  print(currentLoyalty)

  cursor.execute("UPDATE Loyalty SET Bookings = ? WHERE Account_ID = ?", (currentLoyalty,ID))
  connection.commit()

def claimLoyalty(username):
  connection, cursor , locations = connect()

  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]
  
  currentLoyalty -= 10

  print(currentLoyalty)

  if currentLoyalty >= 0:
    cursor.execute("UPDATE Loyalty SET Bookings = ? WHERE Account_ID = ?", (currentLoyalty,ID))
    connection.commit()
    return True
  return False

def checkLoyaltyPoints(username):
  connection, cursor , locations = connect()

  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]

  return [currentLoyalty]