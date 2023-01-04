from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = ""
  return page

@app.route('/blog/hello')
def hb():
  return redirect("/day1")

@app.route('/blog/goodbye')
def gb():
  return redirect("/day2")

@app.route('/day1')
def hello():
  title = "Running Flask"
  date = "4 Jan 2023"
  text = "This is my first time using Flask to program a web server."
  page = ""
  f = open("template/blog.html","r")
  page = f.read()
  f.close()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)

  return page

@app.route('/day2')
def goodbye():
  title = "Leaving Flask"
  date = "5 Jan 2023"
  text = "It was fun while it lasted. Adios, Flask!"
  page = ""
  f = open("template/blog.html","r")
  page = f.read()
  f.close()
  page = page.replace("{title}", title)
  page = page.replace("{date}", date)
  page = page.replace("{text}", text)

  return page

app.run(host='0.0.0.0',port=81)
