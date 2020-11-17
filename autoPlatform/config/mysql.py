def dbConfig():
    """
    数据库配置信息
    :return: 数据字典
    """
    host = "localhost"
    username = "root"
    password = "12345678"
    dbName = "autoPlatform"
    port = 3306
    dbType = "mysql"
    connect = "pymysql"
    return {"host": host, "username": username, "password": password, "db": dbName, "port": port, "db_type": dbType,
            "connect": connect}


def checkValue():
    """
    加密参数
    :return: 加密参数字符串
    """
    return "autoPlatform"
