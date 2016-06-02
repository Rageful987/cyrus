#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)
# routes begin here


@app.route('/')
def hello():
    return "Hello There!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
