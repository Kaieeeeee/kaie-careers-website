from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Kaie"
  
print(__name__)
if __name__ == "__main__":
  print("I am inside if now")
  app.run(host='0.0.0.0', debug=True)