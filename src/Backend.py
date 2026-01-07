from flask import Flask, jsonify, request
from flask_cors import CORS
from components.PythonFunctions.LoginPageFunctions import CreateLogin , LoginCheck

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
  status = CreateLogin(username, password)
  ##
  
  ## Send the status back to the frontend 
  return jsonify({"Status": status})
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
  status, message = LoginCheck(username, password)
  ##
  
  ## Send the status back to the frontend 
  return jsonify({"Status": status,
    "Message": message})
  ##

if __name__ == "__main__":
  app.run(port=5001, debug=True)