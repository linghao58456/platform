"""
@Author: hao.ling
@Date: 2020/11/12 16:22
@Annotation: 配置信息表sql操作
"""

from autoPlatform.dbSql.initialization import initialization


class Configuration(initialization):
    """配置信息相关查询"""

    def insert_config(self, config_name: str, config_path: str, user_id: int):
        """
        新增配置信息
        :param config_name: 配置名称:string
        :param config_path: 配置路径地址:string
        :param user_id: 用户id:int
        :return: 成功：提交，失败：回滚
        """
        try:
            self.cursor.execute(
                f"insert into configurations (config_name,config_path,creatorId) values ('{config_name}',"
                f"'{config_path}',{user_id})")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def select_config(self, config_name: str):
        """
        查询配置信息
        :param config_name: 配置名称;string
        :return:
        """
        self.cursor.execute(f"select * from configurations where config_name={config_name}")
        result = self.cursor.fetchall()
        return result

    def update_config(self, config_name: str, config_path: str, user_id: int):
        """
        更新配置信息
        :param user_id: 修改用户id:int
        :param config_name: 配置名称:string
        :param config_path: 配置路径地址:string
        :return: 成功：提交，失败：回滚
        """
        try:
            self.cursor.execute(
                f"update configurations set config_path={config_path},modifyId={user_id} where config_name={config_name}")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def delete_config(self, config_name: str, status: int, user_id: int):
        """
        删除配置信息
        :param user_id: 修改用户id:int
        :param config_name: 配置名称:string
        :param status: 0:启用,1:禁用
        :return:
        """
        try:
            self.cursor.execute(
                f"update configurations set status={status},modifyId={user_id} where config_name={config_name}")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return True


if __name__ == '__main__':
    conf = Configuration()
    a = conf.insert_config("222", "222", 10002)
    print(a)
