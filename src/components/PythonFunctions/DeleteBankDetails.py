from .BaseFunctions import Databases, connect, Colors

def deleteBankDetails(data):
  connection, cursor , locations = connect()
  
  print(data)

  username = data["UserName"]
  userID = cursor.execute("SELECT Account_ID FROM Accounts WHERE Username = ?", (username,)).fetchone()

  if userID:
    userID = userID[0]

    if cursor.execute("SELECT * FROM Bank_Details WHERE Account_ID = ?", (userID,)).fetchone():
      cursor.execute("DELETE FROM Bank_Details WHERE Account_ID = ?", (userID,))
      
      connection.commit()
      connection.close()

      return {"message": "Success!", "success" : True}
    
    connection.close()
    return {"message" : "No Bank Records!", "success" : False}
      
  return {"message" : "Account Doesnt Exist", "success" : False}