from .BaseFunctions import Databases, connect, Colors

def getBookings(data):
  connection, cursor , locations = connect()
  
  userName = data['UserName']
  userId = cursor.execute("SELECT Account_ID FROM Accounts WHERE Username = ?", (userName,)).fetchone()

  if not userId:
    return {}
  
  userId = userId[0]

  hotelBooking = cursor.execute("SELECT * FROM Hotel_Bookings WHERE Account_ID = ? AND Paid = 1 ORDER BY Booking_ID DESC LIMIT 10", (userId,)).fetchall()
  zooBooking = cursor.execute("SELECT * FROM Zoo_Bookings WHERE Account_ID = ? AND Paid = 1 ORDER BY Booking_ID DESC LIMIT 10", (userId,)).fetchall()

  hotelBookingList = []
  zooBookingList = []

  ## Format the result to look nice
  for i in hotelBooking:
    new = {
    "start_date": i[1],
    "end_date": i[2],
    "room_number": i[3],
    "paid": True if i[8] == 1 else False,
    "cost": i[9],
    "Booking_ID" : i[0]
    }
    hotelBookingList.append(new)

  for i in zooBooking:
    new = {
      "Booking_ID" : i[0],
      "Date" : i[3],
      "Cost": i[9],
      "Adult": i[5],
      "Child": i[6]
    }
    zooBookingList.append(new)
  
  return {"hotel": hotelBookingList, "zoo": zooBookingList}