"""
@Author: hao.ling
@Date: 2020/11/6 14:08
@Annotation: 状态码响应
"""

from flask import jsonify
from . import api


@api.app_errorhandler(400)
def bad_request(e):
    """
    400请求语法错误提示
    :param e:
    :return: json
    """
    return jsonify({"error": "请求语法错误", "code": 400, "data": "", "abnormal": e})


@api.app_errorhandler(404)
def page_not_found(e):
    """
    404没有找到资源提示
    :param e:
    :return: json
    """
    return jsonify({"error": "没有找到资源", "code": 404, "data": "", "abnormal": e})


@api.app_errorhandler(405)
def method_not_allowed(e):
    """
    405请求方法错误提示
    :param e:
    :return: json
    """
    return jsonify({"error": "请求方法错误", "code": 405, "data": "", "abnormal": e})


@api.app_errorhandler(500)
def internal_server_error(e):
    """
    500服务器内部错误提示
    :param e:
    :return: json
    """
    return jsonify({"error": "服务器内部错误", "code": 500, "data": "", "abnormal": e})


@api.app_errorhandler(502)
def bad_gateway(e):
    """
    502网关服务错误
    :param e:
    :return: json
    """
    return jsonify({"error": "网关服务错误", "code": 502, "data": "", "abnormal": e})


@api.app_errorhandler(504)
def gateway_time_out(e):
    """
    504网关请求超时
    :param e:
    :return: json
    """
    return jsonify({"error": "网关请求超时", "code": 504, "data": "", "abnormal": e})
