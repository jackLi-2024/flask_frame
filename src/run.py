#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import time
import json
import logging

from flask import request
from flask import Flask
from flask import jsonify
from flask import render_template

from src.common import output
from src.common import log
from src.common import util

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

sys.path.append("%s/.." % util.home_dir())

log.init_log()
logger = logging.getLogger("flask")


class Handler(object):
    """main handler"""

    def __init__(self):
        self.load_controller_map()

    def load_controller_map(self):
        """load controller obj"""
        self._controller_map = {}
        for root, dirs, files in os.walk("./src/controllers"):
            for name in files:
                if "__init" not in name:
                    controller = None
                    if name[-3:] == ".py":
                        controller = name[:-3]
                    elif name[-4:] == ".pyc":
                        controller = name[:-4]
                    if controller:
                        controller_cls = util.load_cls(
                            "src.controllers", controller)
                        self._controller_map[controller] = controller_cls()

    def handle(self, controller_name, method_name):
        """handle"""
        if controller_name not in self._controller_map:
            return output.error_result(-1, "Module [%s] doesn't exist" % controller_name)
        controller_obj = self._controller_map[controller_name]

        try:
            method = getattr(controller_obj, method_name)
        except AttributeError:
            return output.error_result(-2, "Module [%s] can't find method [%s]"
                                       % (controller_name, method_name))
        try:
            result = method(request)
            if not result or 'status' not in result:
                return output.error_result(-2, u"Method [%s.%s] return Error"
                                           % (controller_name, method_name))
            return result

        except Exception as e:
            return output.error_result(-1, u"Run [%s.%s] defeatly, except: [%s]"
                                       % (controller_name, method_name, e))


handler = Handler()
app = Flask(__name__)
app.debug = True
logger.info("Flask server is ready.")


@app.route('/json/<controller_name>/<method_name>', methods=['GET', 'POST'])
def main_function(controller_name, method_name):
    """main entry"""
    # handle the request
    start_time = time.time()
    result = handler.handle(
        controller_name=controller_name, method_name=method_name)
    end_time = time.time()
    log_content = {
        "cost_time": end_time - start_time,
        "status": result['status'],
        "request": request.args,
        "rs": result.get('log_data', "")
    }
    logger.info(json.dumps(log_content, ensure_ascii=False).encode("utf8"))
    return jsonify(result['response'])

@app.route("/index", methods=["GET"])
def static_html():
    return app.send_static_file("index.html")

@app.route("/hello", methods=["GET"])
def template_html():
    return render_template("test.html")


if __name__ == '__main__':
    # read_dict()
    app.run(host='0.0.0.0', port=8472)
