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
import json
import logging
import signal
import ConfigParser
import time
import sys
from src.common import output
from src.common import util
from src.model.db import db
from src.model.Models import User

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass


class Test():
    def __init__(self):
        pass

    def test1(self, request):
        result = request.args
        db.create_all()
        user = User(username="lijiacai123", email="13112@qq.com")
        db.session.add(user)
        db.session.commit()
        return output.normal_result(result)
