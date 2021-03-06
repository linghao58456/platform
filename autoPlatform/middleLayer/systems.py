from autoPlatform.dbSql.systems import Systems


class System:
    def __init__(self):
        self.config = Systems()

    def select_system_info(self, config_name: str, status=0, start=1, end=10):
        """
        查询配置信息
        :param end: 分页结束
        :param start: 分页开始
        :param config_name: 配置名称:string
        :return:
        """
        m = (int(start) - 1) * int(end)
        n = int(start) * int(end)
        result = self.config.select_config(config_name, status, m, n)
        if len(result) > 0:
            config_dict = []
            for conf in result:
                config_dict.append({"id": conf[0], "system_name": conf[1], "system_path": conf[2], "status": conf[3],
                                    "creatorId": conf[4], "modifyId": conf[5], "create_time": conf[6],
                                    "modify_time": conf[7]})
            return {"code": 1000, "data": config_dict, "message": "success", "total": len(result)}
        return {"code": 9999, "data": {}, "message": "暂无数据", "total": len(result)}

    def insert_system_info(self, config_name: str, config_path: str, user_id: int):
        """
        新增配置信息
        :param config_name: 配置名称:string
        :param config_path: 配置路径地址:string
        :param user_id: 创建用户id:int
        :return:
        """
        result = self.select_system_info(config_name)
        if result['code'] == 9999:
            response = self.config.insert_config(config_name, config_path, user_id)
            if response:
                new_result = self.select_system_info(config_name)
                return {"code": 1000, "data": new_result['data'], "message": "success"}
            return {"code": 9999, "data": {}, "message": "fail"}
        return {"code": 9999, "data": result['data'], "message": "配置名称已存在"}

    def update_system_info(self, config_name: str, config_path: str, user_id: int, system_id: int):
        """
        更新配置信息
        :param system_id: 系统id
        :param config_name: 配置名称:string
        :param config_path: 配置路径地址:string
        :param user_id: 修改用户id:int
        :return:
        """
        response = self.config.update_config(config_name, config_path, user_id, system_id)
        if response:
            result = self.select_system_info(config_name)
            return {"code": 1000, "data": result['data'], "message": "success"}
        return {"code": 9999, "data": {}, "message": "fail"}

    def delete_system_info(self, config_name: str, status: int, user_id: int):
        """
        删除配置信息
        :param config_name: 配置名称:string
        :param status: 0:启用，1:禁用
        :param user_id: 修改用户id:int
        :return:
        """
        result = self.select_system_info(config_name)
        if result['code'] == 1000:
            response = self.config.delete_config(config_name, status, user_id)
            if response:
                new_result = self.select_system_info(config_name)
                return {"code": 1000, "data": new_result['data'], "message": "success"}
            return {"code": 9999, "data": {}, "message": "fail"}
        return result
