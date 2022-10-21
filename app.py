import pymongo
from datetime import datetime
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://monas:171718@cluster0.abcab19.mongodb.net/?retryWrites=true&w=majority") 
db = cluster["orders"]
mycol = db["orders"]
dbcou = cluster["employees"]
mycou = dbcou["couriers"]
from flask import Flask, render_template, request
import os
PEOPLE_FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/')
def index():
    myquery = { "location": "Urago 78" }
    z = []
    p = []
    for x in mycol.find():
        z.append(x)
    pokemons =[]
    for x in mycou.find():
        pokemons.append(x)
    
    return render_template("index.html")

@app.route('/couriers')
def couriers():
    pokemons =[]
    for x in mycol.find():
        pokemons.append(x)
    return render_template("pok.html", len = len(pokemons), pokemons = pokemons)
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        courier = request.form['formSubject']
        
    
    return str(courier)

if __name__ == '__main__':
    app.run()