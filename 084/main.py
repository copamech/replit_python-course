from flask import Flask, request, redirect

# This only works if you are using Replit DB
from replit import db

app = Flask(__name__)

# Checks to see if the user signing up is already in the database. If so, routes back to singup page to try again. If not, allows sign up then moves to login page
@app.route('/signup', methods = ["POST"])
def newUser():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route('/signup')
def signup():  
  page = ""
  f = open("signup.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/login', methods = ["POST"])
def userLogin():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return redirect("/login")
  else:
    if form["password"]==db[form["username"]]["password"]:
      return f"""Hello {db[form["username"]]["name"]}"""
    else:
      return redirect("/login")

@app.route('/login')
def login():
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/')
def index():
  page = ""
  f = open("index.html", "r")
  page = f.read()
  f.close()
  return page

app.run(host='0.0.0.0', port=81)
