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
    status = request.args.get("status")
    currentPage = request.args.get("currentPage")
    pageSize = request.args.get("pageSize")
    response = system.select_system_info(data, status, currentPage, pageSize)
    return jsonify(response)


@api.route("/system/add", methods=["POST"])
def add_system_info():
    data = request.get_json()
    response = system.insert_system_info(data['systemName'], data['systemPath'], data['userId'])
    return jsonify(response)


@api.route("/system/detail", methods=["GET"])
def system_detail_info():
    data = request.args.get("systemName")
    response = system.select_system_info(data)
    return jsonify(response)


@api.route("/system/update", methods=["POST"])
def update_system_info():
    data = request.get_json()
    response = system.update_system_info(data['systemName'], data['systemPath'], data['modifyId'], data['systemId'])
    return jsonify(response)


@api.route("/system/delete", methods=["POST"])
def delete_system_info():
    data = request.get_json()
    response = system.delete_system_info(data['systemName'], data['status'], data['modifyId'])
    return jsonify(response)
