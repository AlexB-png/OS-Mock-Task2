from .BaseFunctions import Databases, connect
import sqlite3 as sql
import datetime

## User class for storing data recieved from fetch request
class user:
  Username = ""
  Date = ""
  Adult = 0
  Child = 0
  MembershipNum = 0
  BookingType = ""
  cost = 0
##

def FormatDateTime(input):
  format = '%Y-%m-%d'
  return datetime.datetime.strptime(input, format)


def DatabaseInteraction(UserClass):
  ## Makes connection to the database file
  connection, cursor , locations = connect()
  ##

  ## Get Current Date
  CurrentDate = datetime.datetime.now()
  ##

  if CurrentDate >= FormatDateTime(UserClass.Date):  ## If input date is before the current date ##
    return {"message":"The Date Is Invalid!", "id": False}
  elif not UserClass.MembershipNum and UserClass.BookingType == 'member':
    return {"message":"The MemberShip Number is empty!", "id": False}
  else: 
    Account_ID = cursor.execute("SELECT Account_ID From Accounts WHERE Username = ?", (UserClass.Username,)).fetchone()[0]
    cursor.execute(f"INSERT INTO {Databases.bookings} (Type_Of_Bookings, Account_ID, Date, Adults, Child, Membership_Number, Username, Cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (UserClass.BookingType, Account_ID, UserClass.Date, UserClass.Adult, UserClass.Child, UserClass.MembershipNum, UserClass.Username, UserClass.cost))
    new_row = cursor.lastrowid
    connection.commit()
    connection.close()
    return {"message":"Success!", "id": new_row}


def GetParams(data):
  UserClass = user()
  
  ## Fills class with user data
  UserClass.Username = data["username"]  ## Username of the user ##
  UserClass.Date = data["date"]  ## Date of the booking ##
  UserClass.BookingType = data["bookingtype"]  ## Visitor / Member / Student ##
  UserClass.MembershipNum = data["membershipnum"]  ## Membership Num if they are a member ##
  UserClass.Adult = data["adult"]  ## How many adults ##
  UserClass.Child = data["child"]  ## How many children ##
  UserClass.cost = data["totalPrice"]  ## Total Cost ##
  ##

  return UserClass  ## Returns the newly created class ##


def MakeZooBooking(data):
  ## Makes the class that contains the user data
  UserClass = GetParams(data)
  ##

  ## Adds data to database and gets a response from the database
  response = DatabaseInteraction(UserClass)
  ##

  return response
