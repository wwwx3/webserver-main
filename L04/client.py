#import Lib
import requests
import json

#Base URL of the server
BASE_URL = "http://localhost:5000"

#Function to get user by ID 
def get_user(user_id):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json())

#Function to add a new user
def add_user(user_data):  
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{BASE_URL}/user", data=json.dumps(user_data), headers=headers)
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json());