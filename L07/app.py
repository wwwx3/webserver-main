import psycopg2
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

host = 'localhost'
dbname = "smart_conveyor"
user = 'wangzhan'
password = '123456789'

app = Flask(__name__)
app.secret_key = "smart_conveyor"

def get_sql_conn():
    return psycopg2.connect(
        host=host,
        database=dbname,
        user=user,
        password=password
    )

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/dashboard")
def dashboard_page():
    return render_template('dashboard.html')

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    user_id = data.get("id")
    password = data.get("password")

    with get_sql_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT password_hash, role FROM users WHERE id = %s;", (user_id,))
            user = cur.fetchone()
    
    if user and check_password_hash(user[0], password):
        session["user_id"] = user_id
        session["role"] = user[1]
        return jsonify({"status": "success!"}), 200

    return jsonify({"status": "error! Invalid credentials"}), 401

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    user_id = data.get("id")
    password = data.get("password")

    hashed = generate_password_hash(password)
    
    try: 
        with get_sql_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (id, password_hash) VALUES (%s, %s);", (user_id, hashed))
        return jsonify({"status": "success!"}), 200
    except Exception:
        return jsonify({"status": "error! User already exists"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
