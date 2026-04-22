import os
import sqlite3
from flask import Flask, request, jsonify, json
from flask_cors import CORS

app = Flask(_name_)
@app.route("/")
def index():
  nazivSpiska="Spisak restorana"
  spisakRestorana=["pastica", "pica tim", "HasHub", "Sahara"]
  return render_template("index.html", naziv=nazivSpiska, spisak=spisakRestorana)


@app.route("/restoran/1")
def restoran():
  nazivRestorana="Meni"
  spisakMenija=["sendvic", "pasta", "pica", "tortilja"]
  return render_template("restoran.html", naziv=nazivRestorana, spisak=spisakMenija)
  

@app.route("/primer-niz")
def niz():
  nekiNiz=[1,2,3,4,5]
@ap.route("/primer-json)
def primerJson():
  data={
    "message": "This is a JSON response",
    "status": "sussess"
  }
