#import libs
from flask import Flask,request

#Flask Setup
app = Flask(__name__)

#Route Setup
@app.route("/")
def home():
    webpage = """
<html>
    <head>
        <title>*✧ Home Page ✧*</title>
    </head>
    <body>
        <h1>（๑˃ᴗ˂）ﻭ ✧ Welcome to the Home Page ✧</h1>
    
    </body>
</html>

    """
    return "This is home page",200


@app.route("/about")
def about():
    return "This is about page",200


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050,debug=True)