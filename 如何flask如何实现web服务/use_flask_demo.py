#! /usr/bin/env python
#-*- coding:utf-8 -*-
#Author: hsh
# 19-3-17  下午2:34

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    print('')