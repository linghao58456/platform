"""
@Author: hao.ling
@Date: 2020/11/10 16:26
@Annotation: 用户登录接口相关
"""
from flask import jsonify, request

from autoPlatform.api import api

from autoPlatform.middleLayer.users import Users

user = Users()


@api.route('/login', methods=["POST"])
def user_Login():
    data = request.get_json()
    response = user.login_user(data['username'], data['password'])
    return jsonify(response)
