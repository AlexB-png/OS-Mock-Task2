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
    return "The Date Is Invalid!"
  elif not UserClass.MembershipNum and UserClass.BookingType == 'member':
    return "The MemberShip Number is empty!"
  else: 
    Account_ID = cursor.execute("SELECT Account_ID From Accounts WHERE Username = ?", (UserClass.Username,)).fetchone()[0]
    cursor.execute(f"INSERT INTO {Databases.bookings} (Type_Of_Bookings, Account_ID, Date, Adults, Child, Membership_Number, Username) VALUES (?, ?, ?, ?, ?, ?, ?)", (UserClass.BookingType, Account_ID, UserClass.Date, UserClass.Adult, UserClass.Child, UserClass.MembershipNum, UserClass.Username))
    connection.commit()
    connection.close()
    return "Success!"


def GetParams(data):
  UserClass = user()
  
  ## Fills class with user data
  UserClass.Username = data["username"]  ## Username of the user ##
  UserClass.Date = data["date"]  ## Date of the booking ##
  UserClass.BookingType = data["bookingtype"]  ## Visitor / Member / Student ##
  UserClass.MembershipNum = data["membershipnum"]  ## Membership Num if they are a member ##
  UserClass.Adult = data["adult"]  ## How many adults ##
  UserClass.Child = data["child"]  ## How many children ##
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
