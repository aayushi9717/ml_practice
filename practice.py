# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:01:48 2019

@author: pcc
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


if __name__ == '__main__':
    app.run(debug=True)