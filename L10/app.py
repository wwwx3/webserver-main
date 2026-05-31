from flask import Flask, render_template , request , jsonify 

app = Flask(__name__)

# Dummy data
sensors_data = {
    "temperature":0,
    "humidity":0,
}
led_state = False 
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API from ESP32 to update sensor data
@app.route('/update', methods=['POST'])
def update_sensors():
    global sensors_data
    data = request.get_json()
    sensors_data["temperature"] = data["temperature"]
    sensors_data["humidity"] = data["humidity"]
    
    return jsonify({
        "status": "ok",
        "led":led_state
    })

#Sensor API 
@app.route("/sensors")
def sensor():
    return jsonify(sensors_data) 

#API to connect the LED
@app.route("/led/<state>")
def led(state):
    global led_state
    if state == "on":
        led_state = True 
    else:
        led_state = False 
    
    return jsonify({"led": led_state})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
    