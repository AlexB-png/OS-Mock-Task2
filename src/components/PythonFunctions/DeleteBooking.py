from .BaseFunctions import Databases, connect, Colors


def deleteBooking(data):
  connection, cursor , locations = connect()

  username = str(data["Username"])
  bookingType = data["BookingType"]
  bookingId = data["BookingId"]

  userId = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not userId:
    return {"message" : "Username Doesn't Exist!"}
  
  userId = userId[0]

  if bookingType == 'zoo':
    if cursor.execute(f"SELECT * FROM {Databases.bookings} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId)).fetchone():
      cursor.execute(f"DELETE FROM {Databases.bookings} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId))
    else:
      return {"message" : "No Bookings Exist!"}
  else:
    cursor.execute(f"DELETE FROM {Databases.hotel_booking} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId))

  connection.commit()
  connection.close()
  
  return {"message" : "Success!"}