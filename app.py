from flask import Flask, render_template, request
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://monas:171718@cluster0.abcab19.mongodb.net/?retryWrites=true&w=majority") 
db = cluster["orders"]
mycol = db["orders"]
dbcou = cluster["employees"]
mycou = dbcou["couriers"]
app = Flask(__name__)
import os
PEOPLE_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/')
def hello_world():

    myquery = { "location": "Urago 78" }
    z = []
    p = []
    style_sheet = os.path.join(app.config['UPLOAD_FOLDER'], 'css/style.min.css')
    courier = os.path.join(app.config['UPLOAD_FOLDER'], 'plugins/images/users/pic0.png')
    logoicon = os.path.join(app.config['UPLOAD_FOLDER'], 'plugins/images/logo-icon.png')
    logotext = os.path.join(app.config['UPLOAD_FOLDER'], 'plugins/images/logo-text.png')
    for x in mycol.find():
        z.append(x)
    pokemons =[]
    for x in mycou.find():
        pokemons.append(x)
    agg_result= mycol.aggregate( 
    [{ 
    "$group" :  
        {"_id" : "null",  
         "Total Subject" : {"$sum" :"$total" } 
         }} 
    ]) 
    for i in agg_result: 
        p.append(i)
   
    return render_template("dashboard.html",p = p, lenz = len(pokemons), style_sheet = style_sheet, pokemons = pokemons, len = len(z), z = z, courier = courier, logotext= logotext, logoicon=logoicon)
if __name__ == '__main__':
    app.run()
