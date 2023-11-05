'''
from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####

number_of_times_clicked = 1

def send_data():
    data = {
        'summary': "You've clicked the button " + str(number_of_times_clicked) + " times.",
        'outcome': "successful"
    }
    number_of_times_clicked += 1 
    return JsonResponse(data)

    
'''
from flask import Flask, request, jsonify
import threading  # Import the threading module

app = Flask(__name__)

import main

# Variable to track the state of data sending
send_data = True

# Function to continuously send data
def continuous_data_sender():
    global send_data
    while True:
        if send_data:
            data = {'fatigued': cnn_running.fatigue_pred(), 'focused': 'add results of model here'}
            yield jsonify(data)
            time.sleep(33) # length of one frame 

@app.route('/endpoint', methods=['POST'])
def toggle_data_sending():
    global send_data
    send_data = not send_data
    return jsonify({'status': 'Data sending ' + ('enabled' if send_data else 'disabled')})

if __name__ == '__main__':
    # Start the continuous data sender in a separate thread
    data_sender_thread = threading.Thread(target=continuous_data_sender)
    data_sender_thread.daemon = True
    data_sender_thread.start()

    app.run(host='0.0.0.0', port=5000)
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def process_request():
    data = request.get_json()
    # Process data here
    response_data = {'result': 'Processed data'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''