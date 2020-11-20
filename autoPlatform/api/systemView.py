"""
@Author: hao.ling
@Date: 2020/11/20 14:53
@Annotation: 系统接口相关
"""
from flask import jsonify, request

from autoPlatform.api import api
from autoPlatform.middleLayer.systems import System

system = System()


@api.route("/getSystem/list", methods=["GET"])
def get_system_list():
    data = request.args.get("systemName")
    print(data)
    response = system.select_system_info(data)
    return jsonify(response)
