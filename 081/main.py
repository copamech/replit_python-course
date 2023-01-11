from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods=["POST"])
def robot():
  form = request.form
  if form['metal'] == "yes":
    return "You're a robot!"
  if "oil" in form['fluid'].lower():
    return "You're a robot!"
  if form['dream'] == "no":
    return "You must be human..."
  else:
    return "You're a robot!"

@app.route('/')
def index():
  page = ""
  f = open("form.html", "r")
  page = f.read()
  f.close()
  return page

app.run(host='0.0.0.0', port=81)
