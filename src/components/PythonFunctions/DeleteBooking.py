from .BaseFunctions import Databases, connect, Colors


## Delete a booking of an account and booking id ##
def deleteBooking(data):
  connection, cursor , locations = connect()

  ## Get data from the request ##
  username = str(data["Username"])
  bookingType = data["BookingType"]
  bookingId = data["BookingId"]

  ## Get User ID from username ##
  userId = cursor.execute(f"SELECT Account_ID FROM {Databases.login} WHERE Username = ?", (username,)).fetchone()
  if not userId:
    return {"message" : "Username Doesn't Exist!"}
  
  ## Make sure its not a list ##
  userId = userId[0]

  ## Find if the booking exists and then delete it for either zoo or hotel ##
  if bookingType == 'zoo':
    if cursor.execute(f"SELECT * FROM {Databases.bookings} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId)).fetchone():
      cursor.execute(f"DELETE FROM {Databases.bookings} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId))
    else:
      return {"message" : "No Bookings Exist!"}
  else:
    if cursor.execute(f"SELECT * FROM {Databases.hotel_booking} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId)).fetchone():
      cursor.execute(f"DELETE FROM {Databases.hotel_booking} WHERE Booking_ID = ? AND Account_ID = ?", (bookingId, userId))
    else:
      return {"message" : "No Bookings Exist!"}

  connection.commit()
  connection.close()
  
  return {"message" : "Success!"}