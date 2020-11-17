"""
@Author: hao.ling
@Date: 2020/11/9 10:19
@Annotation: 中间层用户信息操作
"""
from autoPlatform.dbSql.users import User
from autoPlatform.public.makeMd5 import makeMd5


class Users:
    """用户信息操作"""

    def __init__(self):
        self.user = User()

    def select_user(self, username: str):
        """
        查询用户信息
        :param username: 用户名:string
        :return: 用户信息:dict
        """
        user_info = self.user.select_user_info(username)
        if len(user_info) > 0:
            user_info_list = {}
            for info in user_info:
                user_info_list.update({"user_id": info[0], "username": info[1], "password": info[2], "status": info[3]})
            return {"code": 1000, "data": user_info_list, "message": "success"}
        return {"code": 9999, "data": {}, "message": "用户不存在"}

    def login_user(self, username: str, password: str):
        """
        查询用户名密码
        :param username: 用户名:string
        :param password: 密码:string
        :return: 用户信息:dict
        """
        result = self.select_user(username)
        if result['code'] == 1000:
            newPwd = makeMd5(password)
            if newPwd == result['data']['password']:
                status = 0
                if status == result['data']['status']:
                    return result
                return {"code": 9999, "data": {}, "message": "账号被禁用"}
            return {"code": 9999, "data": {}, "message": "用户名或密码错误"}
        return result

    def insert_user(self, username: str, password: str):
        """
        新增用户
        :param username: 用户名:string
        :param password: 密码:string
        :return: 用户信息:dict
        """
        result = self.select_user(username)
        if result['code'] == 9999:
            newPwd = makeMd5(password)
            response = self.user.insert_user_info(username, newPwd)
            if response:
                new_res = self.select_user(username)
                return new_res
            return {"code": 9999, "data": {}, "message": "fail"}
        return {"code": 9999, "data": result['data'], "message": "用户已存在"}

    def delete_user(self, username: str, status: int):
        """
        删除用户
        :param username: 用户名:string
        :param status: 0:启用,1:禁用
        :return: 用户信息:dict
        """
        result = self.select_user(username)
        if result['code'] == 1000:
            response = self.user.delete_user_info(username, status)
            if response:
                new_res = self.select_user(username)
                return {"code": 1000, "data": new_res['data'], "message": "success"}
            return {"code": 9999, "data": {}, "message": "fail"}
        return {"code": 9999, "data": {}, "message": "用户不存在"}

if __name__ == '__main__':
    user= Users()
    user.insert_user("1212","123123")