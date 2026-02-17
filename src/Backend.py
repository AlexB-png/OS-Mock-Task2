from flask import Flask, jsonify, request
from flask_cors import CORS
from components.PythonFunctions.LoginPageFunctions import CreateLogin , LoginCheck
from components.PythonFunctions.ZooBooking import MakeZooBooking
from components.PythonFunctions.HotelBooking import CreateHotelBooking
from components.PythonFunctions.DeleteAccount import DeleteAccount
from components.PythonFunctions.CheckAdmin import CheckAdmin

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
    "status": response
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

  response = CreateHotelBooking(start, end, username, Guests, Singles, Doubles)

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



## This is the test router for making sure that the app will make a correct fetch request
@app.route("/test", methods=['POST'])
def Test():
  return [True]
##

if __name__ == "__main__":
  app.run(port=5001, debug=True)