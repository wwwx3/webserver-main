from flask import Flask, render_template, request, jsonify, redirect, url_for, session, Response
import cv2
import os
import numpy as np
from datetime import datetime

app = Flask(__name__)
camera_index = 0
SAVE_DIR = "captures"
os.makedirs(SAVE_DIR, exist_ok=True)

camera = cv2.VideoCapture(camera_index)

def open_camera(index):
    global camera, camera_index
    camera_index = index
    if camera is not None:
        camera.release()
    camera = cv2.VideoCapture(camera_index)

def offline_frame():
    frame = np.zeros((480,640,3), dtype=np.uint8)
    cv2.putText(frame, "Camera Offline", (140, 200), cv2.FONT_HERSHEY_SIMPLEX,(0,0,255),2)
    cv2.putText(frame, "Please check the connection", (70, 260), cv2.FONT_HERSHEY_SIMPLEX,(255,255,255),2)
    return frame

def gen_frames():
    while True:
        if camera is None or not camera.isOpened():
            img = offline_frame()
        else:
            success, img = camera.read()
            if not success:
                img = offline_frame()

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('camera.html', cam_index=camera_index)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_camera', methods=['POST'])
def set_camera():
    idx = int(request.json.get("index", 0))
    open_camera(idx)
    return jsonify({"status": "success", "index": idx}), 200

@app.route('/capture', methods=['POST'])
def capture():
    global camera 
    if camera is None or not camera.isOpened():
        return jsonify({"status": "error", "message": "Camera not available"}), 400
    
    success, img = camera.read()
    if not success:
        return jsonify({"status": "error", "message": "Failed to capture image"}), 500
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"IMG_{timestamp}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    cv2.imwrite(filepath, img)
    return jsonify({"status": "saved", "file": filename}), 200

if __name__ == '__main__':
    app.run(host="0.0.0", port=5555, debug=True)
