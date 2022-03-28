from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/')
def index():
    return request.remote_addr

@app.route('/about')
def about():
    return 'About Page Route'