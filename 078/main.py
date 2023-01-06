from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["78"] = {"date": "5 Jan 2023", "link": "https://replit.com/@peircecolin/Python-Day78-Reflections-Webpages?v=1", "reflection": "I have been moving quickly through the html and Flask portions of this 100 day course so I simply reviewed the solution code to further internalize the new information. I don't want to spend too much time coding websites/webpages that I won't use, especially since I would like to revisit the 'portfolio' idea once I have completed the HTML 100 days of code lessons."}

myReflections["79"] = {"date": "6 Jan 2023", "link": "https://replit.com/@peircecolin" ,"reflection": "Coming to you live from the future!"}

@app.route('/<pageNumber>')
def index(pageNumber):
  page = ""
  f = open("template/reflection.html","r")
  page = f.read()
  f.close()
  page = page.replace("{day}", pageNumber)
  page = page.replace("{date}", myReflections[pageNumber]["date"])
  page = page.replace("{link}", myReflections[pageNumber]["link"])
  page = page.replace("{reflection}", myReflections[pageNumber]["reflection"])
  
  return page

app.run(host='0.0.0.0', port=81)
