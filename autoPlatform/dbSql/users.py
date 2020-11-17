"""
@Author: hao.ling
@Date: 2020/11/6 14:07
@Annotation: 用户信息表sql操作
"""

from autoPlatform.dbSql.initialization import initialization


class User(initialization):
    """用户信息相关查询"""

    def set_user_id(self):
        """
        设置user_id从10001开始
        :return: 成功：提交，失败：回滚
        """
        try:
            self.cursor.execute("alter table users AUTO_INCREMENT=10001;")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def select_user_info(self, username: str):
        """
        查询用户信息
        :param username: 用户名:string
        :return: 查询结果:tuple
        """
        self.cursor.execute(f"select user_id,username,password,status from users where username='{username}'")
        response = self.cursor.fetchall()
        return response

    def insert_user_info(self, username: str, password: str):
        """
        新增用户信息
        :param username: 用户名:string
        :param password: 密码:string
        :return: 成功：提交，失败：回滚
        """
        try:
            self.cursor.execute(f"insert into users (username,password,status) values ('{username}','{password}',0)")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def delete_user_info(self, username: str, status: int):
        """
        删除用户
        :param username: 用户名:string
        :param status: 0:启用,1:禁用
        :return:
        """
        try:
            self.cursor.execute(f"update users set status={status} where username={username}")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False


if __name__ == '__main__':
    user = User()
    a = user.insert_user_info("admin", "123123")
    print(a)
