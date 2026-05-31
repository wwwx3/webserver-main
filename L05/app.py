#import Lib 
from flask import Flask,render_template, request, jsonify,session, redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
import csv

#Initialize Flask app
app = Flask(__name__)

#Secret key for session management
app.secret_key ="welcome to flask session"

#Path Settings
Base_DIR = os.path.dirname(os.path.abspath(__file__))

#Database Path
DB_FOLDER = os.path.join(Base_DIR,"database")

#Data files 
USER_FILE = os.path.join(DB_FOLDER,"users.json")
STUDENT_FILE = os.path.join(DB_FOLDER,"students.csv")

#CSV Headers
#Primary key: ID 
FIELDS = ["ID","Name","Survay","Grade"]


#Initialize Database (DB = database)
def init_db():
    #Check if database folder exists
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    
    #Check if user file exists
    if not os.path.exists(USER_FILE):
        #Using  utf-8 for encoding Thai characters
        with open(USER_FILE,mode='w',newline='',encoding='utf-8') as f:
            json.dump({},f)
            print("User database created.")

    #Check if student file exists
    if not os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE,mode='w',newline='',encoding='utf-8') as f:
            #Create a DictWriter object
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            
            #Create the header rows
            writer.writeheader()
            print("Student database created.")

#Call the init_db functiion 
init_db()


#Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route("/register_page")
def register_page():
    return render_template("register.html")

#API Endpoints note : Should only return to the server.
@app.route("/api/login", methods=["POST"])
def login() :
    data = request.json
    username = data.get("username")
    password = data.get("password")

    #Load user data from CSV file
    with open(USER_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)

    #Check if username already exists (Need fixing)
    if any(user["username"] == username for user in users):
        return jsonify({"errors": "User already exists."}),400 
    
    #Hash Password 
    users.append({
        "username": username,
        "password": generate_password_hash(password)
    })
    
    #Save Users 
    with open(USER_FILE, 'w',encoding='utf-8') as f:
        json.dump(users,f,indent=4)

    return jsonify({"message":"Registration successful."}),201 

#Run the Flask app 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)