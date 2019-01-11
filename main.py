import os
from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient
MONGO_URL = os.environ.get('mongodb://heroku:ZjLlx4Vo8ndAed-4nX5k-OkoYsT5VB2MGa-taN0byrmyrSLt8OhcGz0CVReUDDfjxd9rRA3QQc0IhE8H9X8hSQ@candidate.66.mongolayer.com:10279,candidate.61.mongolayer.com:11249/app121630054')
client = MongoClient(MONGO_URL)

db = client.app121630054
collection = db.shoutouts

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    shouts = collection.find()
    return render_template('index.html', shouts=shouts)

@app.route("/post", methods=['POST'])
def post():
    shout = {"name":request.form['name'], "message":request.form['message']}
    shout_id = collection.insert(shout)
    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)