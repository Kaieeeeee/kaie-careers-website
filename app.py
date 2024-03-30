from flask import Flask, render_template
app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Quezon City, Philippines',
    'salary':' 10,000 Pesos'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Caloocan City, Philippines',
    'salary':' 15,000 Pesos'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':' 12,000 Pesos'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'New York, USA',
    'salary':'$15,000'
  },
  
]
@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)
  
print(__name__)
if __name__ == "__main__":
  print("I am inside if now")
  app.run(host='0.0.0.0', debug=True)