# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:36:54 2023

@author: compl
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"