from flask import Flask, render_template, request
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://monas:171718@cluster0.abcab19.mongodb.net/?retryWrites=true&w=majority") 
db = cluster["orders"]
mycol = db["orders"]
app = Flask(__name__)

@app.route('/')
def hello_world():
     myquery = { "location": "Urago 78" }
    z = []
    p = []
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
   
    return render_template("dashboard.html",p = p, lenz = len(pokemons), pokemons = pokemons, len = len(z), z = z)
if __name__ == '__main__':
    app.run()
