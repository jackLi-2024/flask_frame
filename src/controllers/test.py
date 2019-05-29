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
from src.model.Models import *

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

logger = logging.getLogger("flask")


class Test():
    def __init__(self):
        pass

    def test1(self, request):
        result = request.args
        return output.normal_result(result)
