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

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def process_request():
    data = request.get_json()
    # Process data here
    response_data = {'result': 'Processed data'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)