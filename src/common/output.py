#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""
import json
import sys
import os

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass


def normal_result(data=None, log_data=None):
    """normal result"""
    response = {
        'status': 0,
        'msg': "success",
        'data': data
    }
    result = {
        'status': 0,
        'response': response,
        'log_data': log_data
    }
    return result


def error_result(error_code, error_msg):
    """error result"""
    response = {
        'status': error_code,
        'msg': error_msg,
    }
    result = {
        'status': error_code,
        'response': response,
        'log_data': response
    }
    return result
