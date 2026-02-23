from .BaseFunctions import Databases, connect, Colors
from .LoyaltySystem import LoyaltySystem

def makePayment(data, username):
  bookedRoomNumber = data["RoomNumber"]

  cardName = data["CardName"]
  cardNum = data["CardNum"]
  cvv = data["CVV"]
  expiry = data["Expiry"]
  billingAddress = data["BillAddress"]
  loyalty = data["Loyalty"]

  bookingID = data["RoomNumber"]

  print(bookingID)

  bookingType = data["BookingType"]

  if (not loyalty):
    if len(cardNum) != 16:
      return {"message": "Card number is not 16 digits", "success": False}
    elif len(cvv) != 3:
      return {"message": "CCV is not 3 digits long", "success": False}

  addResponse = addToDB(cardName, expiry, billingAddress, username, bookingType, bookingID)
  return {"message": "Success!", "success": True}


def addToDB(cardName, expiry, billingAddress, username, bookingType, bookingID):
  connection, cursor , locations = connect()

  account_id = cursor.execute("SELECT Account_ID FROM Accounts WHERE Username = ?", (username,)).fetchone()[0]

  cursor.execute("INSERT INTO Bank_Details (Name,Expiration,Address,Account_ID) VALUES (?,?,?,?)", (cardName, expiry, billingAddress, account_id))

  if bookingType == "hotel":
    cursor.execute(
      "UPDATE Hotel_Bookings SET Paid = 1 WHERE Booking_ID = ?",
      (bookingID,)
    )
  else:
    cursor.execute(
      "UPDATE Zoo_Bookings SET Paid = 1 WHERE Booking_ID = ?",
      (bookingID,)
    )

  connection.commit()
  connection.close()

  LoyaltySystem(username)