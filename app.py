import os
import sqlite3
from flask import Flask, request, jsonify, json
from flask_cors import CORS

app = Flask(_name_)
@app.route("/")
def index():
  return "Zdravo brate"
@app.route("/primer-string")
def string():
  return "Neki ne preterano dugacak text"
@app.route("/primer-broj")
def broj():
  return"125"
if_name_ == "_main_"
@app.route("/primer-niz")
def niz():
  nekiNiz=[1,2,3,4,5]
@ap.route("/primer-json)
def primerJson():
  data={
    "message": "This is a JSON response",
    "status": "sussess"
  }
