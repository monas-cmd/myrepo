from flask import Flask, render_template, request
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://monas:171718@cluster0.abcab19.mongodb.net/?retryWrites=true&w=majority") 
db = cluster["orders"]
mycol = db["orders"]
app = Flask(__name__)

@app.route('/')
def hello_world():
    z = []
    p = []
    for x in mycol.find():
        z.append(x)
    return render_template('index.html', z = str(z) )
if __name__ == '__main__':
    app.run()
