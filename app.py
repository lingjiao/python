#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by lingjiao.lc

"""
Note, in my script, a tab equals four blanks.
You must have a check of your indentation.
"""

import os
import sys
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def hello_world1():
    return 'Hello World, 123!'

@app.route('/webhook')
def helloworld():
    return 'Hello World, webhook complete!'

@app.route('/user/<path:name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/test')
def test():
    print dir(request)
    username = request.args.get('username')
    return '<h1>hello, %s!</h1>' % username

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
