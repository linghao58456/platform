"""
@Author: hao.ling
@Date: 2020/11/6 14:08
@Annotation: 服务应用层
"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from autoPlatform.config.mysql import dbConfig
from autoPlatform.dbSql.users import User

db = SQLAlchemy()

database = dbConfig()
user = User()


def create_app():
    """
    创建项目实例
    :return: app实例
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{database['db_type']}+{database['connect']}://{database['username']}:" \
                                            f"{database['password']}@{database['host']}:{database['port']}/" \
                                            f"{database['db']}"
    db.init_app(app)
    create_tables(app)
    user.set_user_id()

    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    注册蓝图
    :param app: 项目应用名称
    :return:
    """
    from autoPlatform.api import api

    CORS(api, supports_credentials=True)
    app.register_blueprint(api, url_prefix='/api')


def create_tables(app):
    """
    创建数据库表结构模型
    :param app: 项目应用名称
    :return:
    """
    from autoPlatform.dataModel.users import Users
    from autoPlatform.dataModel.system import System

    db.create_all(app=app)
