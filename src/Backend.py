from flask import Flask, jsonify, request
from flask_cors import CORS
from components.PythonFunctions.LoginPageFunctions import CreateLogin , LoginCheck
from components.PythonFunctions.BookingFunctions import MakeBooking

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


## This is the hotel booking route
@app.route("/booking", methods=['POST'])
def Booking():
  data = request.get_json()

  username = data.get("user")  ## Username of user
  start = data.get("start")  ## Start Date
  end = data.get("end")  ## End Date 
  booking_type = data.get("type")  ## Hotel or Zoo

  MakeBooking(username, start, end, booking_type)

  return "This has to be here to stop a CORS error"
##

## This is the Zoo Booking route
@app.route("/zoobooking", methods=['POST'])
def zooBooking():
  data = request.get_json()
  print(data)

  return {
    "status": True
  }
##

## This is the test router for making sure that the app will make a correct fetch request
@app.route("/test", methods=['POST'])
def Test():
  return [True]
##

if __name__ == "__main__":
  app.run(port=5001, debug=True)