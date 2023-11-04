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