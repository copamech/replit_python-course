from flask import Flask, request ###### Didn't import 'request'

app = Flask(__name__)

logins = {}
logins["alice"] = {"email": "alice@aol.com", "password": "wonderland"}
logins["bob"] = {"email": "bob@aol.com", "password": "youruncle"}
logins["carol"] = {"email": "carol@aol.com", "password": "xmasdickens"}

@app.route("/login", methods=["POST"])

def login():
  page = ""
  form = request.form
  details = {}

  try:
    details = logins[form["username"]]
  except:
    return "Username, email or password incorrect"

  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email or password incorrect"

  return page


@app.route('/')
def index():
  page = """

  <form method="post" action="/login">
    
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Login</button>
    
  </form>    
    
    """
  return page
  
app.run(host='0.0.0.0', port=81)
