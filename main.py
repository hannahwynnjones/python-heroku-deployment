import os
from flask import Flask, render_template, request, redirect
import pymongo
from pymongo import MongoClient
MONGO_URL = os.environ.get('mongohq-transparent-95617')
client = MongoClient(MONGO_URL)

db = client.app121630054
collection = db.shoutouts

app = Flask(name)

@app.route("/", methods=['GET'])
def index():
    shouts = collection.find()
    return render_template('index.html', shouts=shouts)

@app.route("/post", methods=['POST'])
def post():
    shout = {"name":request.form['name'], "message":request.form['message']}
    shout_id = collection.insert(shout)
    return redirect('/')

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




# db = client.
# collection = db.shoutouts
#
#
# @app.route("/", methods=['GET'])
# def index():
#     print('Hello World!')
#     shouts = collection.find()
#     return render_template('index.html', shouts=shouts)
#
#
# @app.route("/post", methods=['POST'])
# def post():
#     print('POST request')
#     shout = {"name":request.form['name'], "message":request.form['message']}
#     shout_id = collection.insert(shout)
#     return redirect('/')
#
# app = Flask(name)
#
#
# if name == "main":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
#
#
#
# app = Flask(__name__)
#
# # @app.route("/")
# # def hello():
# #     return "Hello world!"
# #
# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(host='0.0.0.0', port=port)
