from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:8080")

@app.route('/')
def get_data():
    data = {'message': 'Hello from Flask!'}
    return (data)

@app.route('/hello')
def hello():
    return 'Hello, World'
