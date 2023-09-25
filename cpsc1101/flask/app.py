# Simple web server to store logged in data in memory using web components with HTMX on frontend

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():

    # Get the username and password from the request body
    Username = request.form.get('username')
    Password = request.form.get('password')

    if (not Username or not Password):
        return LoginElement("Missing username or password", False).ToHTML()

    # Create a new user from the username and password

    CreatedUser = user(Username, Password)

    return LoggedInElement("Logged in successfully", True, CreatedUser).ToHTML()

# Since we're not using files, if program restarts, all data is lost 

class user: 

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.data = { }
    
    def AddData(self, key, value):
        self.data[key] = value

class LoginElement:

    def __init__(self, message, success):
        self.message = message
        self.success = success

    def ToHTML(self): 
        return f"""            
        <label for="username">Username</label>
            <input type="text" name="username" id="username"/> 
        <br/>
        <br>
            <label for="password">Password</label>
            <input type="password" name="password" id="password"/> 
        <br/>
        <br>

        {self.success and f"<p>{self.message}</p>" or f"<p style='color: red;'>{self.message}</p>"}

        <input type="submit" name="submit" id="submit" value="Login"/> 
        """

class LoggedInElement:

    def __init__(self, message, success, user):
        self.message = message
        self.success = success
        self.user = user

    def ToHTML(self): 
        return f"""            
        <div class="LoggedInElement"/>
            <p>Logged in successfully</p>
            <p>Username: {self.user.username}</p>
            <p>Password: {self.user.password}</p>
        """