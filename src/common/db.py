#!/usr/bin/python
# coding:utf-8

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass


app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@52.82.8.156:9906/lijiacai_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    db.create_all()
    user = User(username="lijiacai", email="11@qq.com")
    db.session.add(user)
    db.session.commit()
