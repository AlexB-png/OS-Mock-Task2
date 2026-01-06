from .BaseFunctions import Databases, connect
import sqlite3 as sql
import bcrypt

## Check whether the username and password is correct ##
def LoginCheck(username, password):
  connection, cursor , locations = connect()
  data = cursor.execute(f"SELECT Password FROM {locations.login} WHERE Username = ?",(username,)).fetchall()
  
  ## Compare the hashed passwords

  ## convert input to bytes
  byte = str(password).encode("UTF-8")
  ##

  ## If the hashed password in Database matches bytes 
  if bcrypt.checkpw(byte, data[0][0]):  ## data is stored as [(DATA)] ##
    return True
  else:
    return False
  ##
##

## Create an account ##
def CreateLogin(username, password):
  connection, cursor , locations = connect()

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
  except sql.IntegrityError:
    return False
  ##

  connection.commit()
  connection.close()
##