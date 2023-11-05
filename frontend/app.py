from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import cv2
import base64

app = Flask(__name__)
socketio = SocketIO(app)

send_data = True

def generate():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = base64.b64encode(buffer)
            yield f'data:image/jpeg;base64,{frame_bytes.decode("utf-8")}'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle_data_sending')
def toggle_data_sending():
    global send_data
    send_data = not send_data
    emit('status_update', {'status': 'Data sending ' + ('enabled' if send_data else 'disabled')})

@socketio.on('connect')
def handle_connect():
    emit('status_update', {'status': 'Connected'})

@socketio.on('disconnect')
def handle_disconnect():
    emit('status_update', {'status': 'Disconnected'})

if __name__ == '__main__':
    socketio.start_background_task(target=continuous_data_sender)
    socketio.run(app, host='0.0.0.0', port=5000)
