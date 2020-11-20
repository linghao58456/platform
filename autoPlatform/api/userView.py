"""
@Author: hao.ling
@Date: 2020/11/10 16:26
@Annotation: 用户接口相关
"""
from flask import jsonify, request

from autoPlatform.api import api

from autoPlatform.middleLayer.users import Users

user = Users()


@api.route('/login', methods=["POST"])
def user_login():
    data = request.get_json()
    response = user.login_user(data['username'], data['password'])
    return jsonify(response)


@api.route('/register', methods=["POST"])
def user_register():
    data = request.get_json()
    response = user.insert_user(data['username'], data['password'])
    return jsonify(response)


@api.route('/searchUser', methods=["GET"])
def user_search():
    data = request.args.get("username")
    response = user.select_user(data)
    return jsonify(response)


@api.route('/resetPwd', methods=["POST"])
def user_reset():
    data = request.get_json()
    response = user.update_user_password(data['username'], data['password'])
    return jsonify(response)


@api.route('/changePwd', methods=["POST"])
def user_change():
    data = request.get_json()
    response = user.change_user_password(data['username'], data['oldPwd'], data['newPwd'])
    return jsonify(response)
