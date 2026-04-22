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


@app.route("/restorani")
def restorani():
  nazivRestorana="Spisak restorana"
  spisakMenija=["pastica", "pica tim", "HasHub", "Sahara"]
  return render_template("restorani.html", naziv=nazivRestorana, spisak=spiakMenija)
  
@app.route("/restorani/1")
def meni():
  nazivMeni="Meni restorana"
  spisakMeni=["pastica", "pica tim", "HasHub", "Sahara"]
  return render_template("meno.html", naziv=nazivMeni, spisak=spisakMeni)
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
