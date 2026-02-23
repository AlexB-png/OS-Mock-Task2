from flask import Flask, jsonify, request
from flask_cors import CORS
from components.PythonFunctions.LoginPageFunctions import CreateLogin , LoginCheck
from components.PythonFunctions.ZooBooking import MakeZooBooking
from components.PythonFunctions.HotelBooking import CreateHotelBooking
from components.PythonFunctions.DeleteAccount import DeleteAccount
from components.PythonFunctions.CheckAdmin import CheckAdmin
from components.PythonFunctions.MakePayment import makePayment
from components.PythonFunctions.DeleteBooking import deleteBooking
from components.PythonFunctions.GetBookings import getBookings
from components.PythonFunctions.DeleteBankDetails import deleteBankDetails

app = Flask(__name__)
CORS(app)

@app.route("/createaccount", methods=["POST"])
def CreateAccount():
  ## Get the {} json from the frontend
  data = request.get_json()
  ##

  ## Process the dictionary
  username = data.get("username")
  password = data.get("password")
  ##

  ## Returns a status message based on success or failure
  status, Color = CreateLogin(username, password)
  ##
  
  ## Send the status back to the frontend 
  return jsonify({"Status": status,
  "Color": Color})
  ##

@app.route("/login", methods=["POST"])
def Login():
  ## Get the {} json from the frontend
  data = request.get_json()
  ##

  ## Process the dictionary
  username = data.get("username")
  password = data.get("password")
  ##

  ## Returns a status message based on success or failure
  status, message, color = LoginCheck(username, password)
  ##
  
  ## Send the status back to the frontend 
  return jsonify({"Status": status,
    "Message": message,
    "Color":color})
  ##

## This is the Zoo Booking route
@app.route("/zoobooking", methods=['POST'])
def zooBooking():
  data = request.get_json()

  response = MakeZooBooking(data)

  return {
    "status": response["message"],
    "id": response["id"]
  }
##

@app.route("/hotelbooking", methods=['POST'])
def HotelBooking():
  data = request.get_json()

  start = data["start"]
  end = data["end"]
  username = data["user"]

  Guests = data["guests"]
  Singles = data["singles"]
  Doubles = data["doubles"]

  cost = data["totalPrice"]

  response = CreateHotelBooking(start, end, username, Guests, Singles, Doubles, cost)

  status = response[0]
  success = response[1]
  rowid = response[2]
  
  print(response)

  return {
    "Status" : status,
    "Success" : success,
    "rowid" : rowid
  }

@app.route("/deleteaccount", methods=['POST'])
def DeleteUserAccount():
  data = request.get_json()
  username = data['username']

  response = DeleteAccount(username)

  print(response['status'])

  return { "Status" : response['status'], "message" : response["message"] }

@app.route("/checkadmin", methods = ['POST'])
def CheckIfAdmin():
  data = request.get_json()
  username = data["username"]

  status = CheckAdmin(username)

  return {'status' : status}

@app.route("/payment", methods = ['POST'])
def MakePaymentToDB():
  data = request.get_json()

  userName = data["Username"]

  response = makePayment(data, userName)

  return response

@app.route("/cancel", methods = ["POST"])
def CancelBooking():
  data = request.get_json()

  reponse = deleteBooking(data)

  return reponse

@app.route("/checkbookings", methods = ["POST"])
def CheckBookings():
  data = request.get_json()

  response = getBookings(data)
  
  return response

@app.route("/deletebankdetails", methods = ['POST'])
def DeleteBankDetails():
  data = request.get_json()

  response = deleteBankDetails(data)

  return response

## This is the test router for making sure that the app will make a correct fetch request
@app.route("/test", methods=['POST'])
def Test():
  data = request.get_json()
  print(data)
  
  return [True]
##

if __name__ == "__main__":
  app.run(port=5001, debug=True)