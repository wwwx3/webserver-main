from flask import Flask, request,jsonify
import json
app = Flask(__name__)
DATA_FILE ='user.json'

def load_users():
    with open(DATA_FILE,'r',encoding ='utf-8') as f:
        return json.load(f)
    
    @app.route("/user/<int:user_id>",methods=['POST'])
    def add_user():
        incoming_user = request.json
        users = load_users()
        users.append(incoming_user)
        save_users(users)
    return jsonify(users[user_id]), 201

@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    data = request.json
    users = load_users()

    for user in users:
        if user['id'] == user_id:
            user.update(data)
            save_users(users)
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404