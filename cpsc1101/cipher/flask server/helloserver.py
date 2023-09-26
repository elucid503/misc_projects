from flask import Flask

# Create instance of the flask class, the first argument is the name of the applications package __name__ is a convenient shortcut
app = Flask(__name__)

# Use route decorator to tell Flask what URL should trigger our function
@app.route("/")

# The function triggers the message we want to trigger on the user's browser
def hello_world():
    return "<p>Hello, World!</p>"