from flask import Flask, request, jsonify

from dotenv import load_dotenv

import json
import requests
import os
from flask_cors import CORS
from mongo import create_user, auth_user

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return "<p>main endpoint done</p>"

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username", [])
    password = data.get("password", [])
    create_user(username, password)
    return jsonify({"message": "User created successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username", [])
    password = data.get("password", [])
    resp = auth_user(username, password)

    if resp:
        resp["password"] = password
        return jsonify({"message": "User authenticated", "user": resp})
    else:
        return jsonify({"message": "Username or Password is incorrect."})
    

if __name__ == "__main__":
    app.run(debug=True)