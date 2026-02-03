from .BaseFunctions import Databases, connect, Colors
import sqlite3 as sql

## User class for storing data recieved from fetch request
class user:
  Username = ""
  Date = ""
  Adult = 0
  Child = 0
  MembershipNum = 0
  BookingType = ""
##

def GetParams(data):
  UserClass = user()
  
  UserClass.Username = data["username"]
  UserClass.Date = data["date"]
  UserClass.BookingType = data["bookingtype"]
  UserClass.MembershipNum = data["membershipnum"]
  UserClass.Adult = data["adult"]
  UserClass.Child = data["child"]

  return UserClass


def MakeBooking(data):
  print(GetParams(data).Child)
