from .BaseFunctions import Databases, connect, Colors

def LoyaltySystem(username):
  connection, cursor , locations = connect()

  ## Get Account ID from username ##
  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  ## Get Loyalty Points of the user ## 
  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  ## If the user hasnt claimed points before add them to database ##
  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]
  
  currentLoyalty += 1

  ## Update the loyalty points ##
  cursor.execute("UPDATE Loyalty SET Bookings = ? WHERE Account_ID = ?", (currentLoyalty,ID))
  connection.commit()

def claimLoyalty(username):
  connection, cursor , locations = connect()

  ## Get the account ID from the username ##
  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  ## Check if user exists in the loyalty database ##
  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]
  
  ## Take away 10 points ##
  currentLoyalty -= 10

  ## Update database with new points if its more than or equal to 10 ##
  if currentLoyalty >= 0:
    cursor.execute("UPDATE Loyalty SET Bookings = ? WHERE Account_ID = ?", (currentLoyalty,ID))
    connection.commit()
    return True
  return False

def checkLoyaltyPoints(username):
  connection, cursor , locations = connect()

  ## Get account ID from username ##
  ID = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not ID:
    return {"message" : "Username Doesn't Exist!"}
  
  ID = ID[0]

  ## get current loyalty points ##
  currentLoyalty = cursor.execute("SELECT Bookings FROM Loyalty WHERE Account_ID = ?", (ID,)).fetchone()

  ## If user doesnt exist in the db ##
  if not currentLoyalty:
    cursor.execute("INSERT INTO Loyalty (Account_ID, Bookings) VALUES (?, ?)",(ID, 0))
    currentLoyalty = 0
  else:
    currentLoyalty = currentLoyalty[0]

  return [currentLoyalty]