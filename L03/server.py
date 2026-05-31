#Import 
from flask import Flask, render_template

#Flask Setup
app = Flask(__name__)

#Add Routes 
@app.route("/")
def home():
    return render_template("index.html")

#Run flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
