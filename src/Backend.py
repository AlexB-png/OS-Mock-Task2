from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/createaccount", methods=["POST"])
def CreateAccount():
  data = request.get_json()

  username = data.get("username")
  password = data.get("password")
  
  return jsonify({"Status": True})

@app.route("/test")
def CheckOnline():
  return jsonify({"Test":True})

if __name__ == "__main__":
  app.run(port=5001, debug=True)