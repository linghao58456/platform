"""
@Author: hao.ling
@Date: 2020/11/5 15:26
@Annotation: api蓝图
"""
from flask import Blueprint

api = Blueprint("api", __name__)

from autoPlatform.api import errors, userView, systemView
