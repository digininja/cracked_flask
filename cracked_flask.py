from flask import Flask, session
from waitress import serve

app = Flask(__name__)

# This is very important, keep this really secret!
app.config['SECRET_KEY'] = 'monkey'

@app.route('/')
def index():
    session['hello'] = "world"
    if not 'username' in session:
        session['username'] = "robin"

    if session['username'] == "admin":
        ret_str = "Welcome back administrator"
    else:
        ret_str = "Welcome back "+ session["username"]
        
    return ret_str + "\n"

def create_app():
    return app

if __name__ == "__main__":
    # serve(app, host="127.0.0.1", port=5000)
    serve(app, port=5000)
