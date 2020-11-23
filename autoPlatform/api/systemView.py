"""
@Author: hao.ling
@Date: 2020/11/20 14:53
@Annotation: 系统接口相关
"""
from flask import jsonify, request

from autoPlatform.api import api
from autoPlatform.middleLayer.systems import System

system = System()


@api.route("/system/list", methods=["GET"])
def get_system_list():
    data = request.args.get("systemName")
    currentPage = request.args.get("currentPage")
    pageSize = request.args.get("pageSize")
    response = system.select_system_info(data, currentPage, pageSize)
    return jsonify(response)


@api.route("/system/add", methods=["POST"])
def add_system_info():
    data = request.get_json()
    response = system.insert_system_info(data['systemName'], data['systemPath'], data['userId'])
    return jsonify(response)
