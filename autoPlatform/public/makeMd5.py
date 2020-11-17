"""
@Author: hao.ling
@Date: 2020/11/10 15:10
@Annotation: md5加密方式
"""
import hashlib

from autoPlatform.config.mysql import checkValue


def makeMd5(password: str):
    """
    md5加密
    :param password: 密码:string
    :return: 大写加密字符串:string
    """
    key = checkValue()
    value = key + password
    result = hashlib.md5(value.encode("utf-8")).hexdigest()
    return result.upper()
