from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():

    print("Login Route Requested!")
    return "Login Route"