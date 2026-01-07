from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql
import bcrypt

## Check whether the username and password is correct ##
def LoginCheck(username, password):
  connection, cursor , locations = connect()
  data = cursor.execute(f"SELECT Password FROM {locations.login} WHERE Username = ?",(username,)).fetchall()
  
  if data:
    ## Compare the hashed passwords

    ## convert input to bytes
    byte = str(password).encode("UTF-8")
    ##

    ## If the hashed password in Database matches bytes 
    if bcrypt.checkpw(byte, data[0][0]):  ## data is stored as [(DATA)] ##
      return True, "Successfully Logged In", Colors.green
    else:
      return False, "Incorrect Password", Colors.red
    ##
  else:
    ## Return False if the input username doesnt exist ##
    return False, "Username Does Not Exist", Colors.red
##

## Create an account ##
def CreateLogin(username, password):
  connection, cursor , locations = connect()

  ## Pass must be 8 characters or more
  if len(password) < 8:
    return "Password must be 8+ characters", Colors.red
  elif len(username) < 5:
    return "Username needs to be 5+ characters", Colors.red
  ##

  ## Hash the password
  byte = str(password).encode("UTF-8")

  ## Generate the salt ##
  salt = bcrypt.gensalt()
  ##

  hashed = bcrypt.hashpw(byte, salt)
  ##
  
  ## Try creating the login // If exists fail // else create the login ##
  try:
    status = cursor.execute(f"INSERT INTO {locations.login} (Username, Password) VALUES (?,?)",(username,hashed))
    
    connection.commit()
    connection.close()
    
    return "Successfully created", Colors.green
  except sql.IntegrityError:  ## If there is no possible UNIQUE username key ##
    connection.close()
    return "Username is already in use", Colors.red
  ##
##