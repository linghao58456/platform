"""
@Author: hao.ling
@Date: 2020/11/12 14:21
@Annotation: 配置中心表
"""

from autoPlatform.config.service import db
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey


class System(db.Model):
    __tableName__ = "system"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="配置id")
    config_name = Column(String(64), nullable=False, unique=True, comment="配置名称")
    config_path = Column(String(64), nullable=True, comment="配置路径地址")
    status = Column(Boolean, server_default="0", comment="当前账户状态(0:启用,1:禁用)")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=True, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=True, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
