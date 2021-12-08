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

    return '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<title>Cracked Flask Lab</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="shortcut icon" type="image/png" href="https://digi.ninja/favicon.ico" />
		<link href="/css/style.css" rel="stylesheet" type="text/css" />

		<meta name="Description" content="A lab to learn about Python Flask sessions." />
		<meta name="Keywords" content="flask,python,crack,session,site,security,ethical,hacking,penetration,testing,website,application,ninja,digininja" />

		<meta property="og:title" content="DigiNinja - Cracked Flask Lab" />
		<meta property="og:description" content="A lab to learn about Python Flask sessions." />
		<meta property="og:url" content="/index.php" />
		<meta property="og:image" content="https://digi.ninja/graphics/twittercards/cracked_flask_twittercard.png" />
		<meta property="og:type" content="website" />
		<meta property="og:sitename" content="DigiNinja" />

		<meta name="twitter:card" content="summary" />
		<meta name="twitter:title" content="DigiNinja - Cracked Flask Lab" />
		<meta name="twitter:description" content="A lab to learn about Python Flask sessions." />
		<meta name="twitter:site" content="@digininja" />
		<meta name="twitter:creator" content="@digininja" />
		<meta name="twitter:domain" content="digi.ninja" />
		<meta name="twitter:site" content="@digininja" />
		<meta name="twitter:image" content="https://digi.ninja/graphics/twittercards/cracked_flask_twittercard.png" />
	</head>
	<body>
		<h1>Cracked Flask Lab</h1>
    <p>Welcome to the Cracked Flask Lab.</p>
    <p>The challenge is easy, crack the Flask session and become an administrator.</p>
    <p><a href="/user">Enter the lab</a></p>

		<hr />
		<p>
			Lab created by Robin Wood - <a href="https://digi.ninja">DigiNinja</a>
		</p>
	</body>
</html>
    '''

@app.route('/user')
def user():
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
