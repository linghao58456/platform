"""
@Author: hao.ling
@Date: 2020/11/6 14:07
@Annotation: 数据库连接初始化
"""

import pymysql
from autoPlatform.config.mysql import dbConfig


class initialization:
    """数据库连接初始化方法"""

    def __init__(self):
        """初始化数据库连接"""
        database = dbConfig()
        self.db = pymysql.Connect(host=database['host'], user=database['username'], password=database['password'],
                                  port=database['port'], database=database['db'])
        self.cursor = self.db.cursor()
