"""
@Author: hao.ling
@Date: 2020/11/27 14:23
@Annotation: 场景z
"""

from autoPlatform.config.service import db
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey


class Scenes(db.Model):
    __tableName__ = "scenes"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="场景id")
    scene_name = Column(String(64), nullable=False, unique=True, comment="场景名称")
    scene_step = Column(String(255), nullable=True, comment="场景步骤")
    status = Column(Boolean, nullable=False, server_default=0, comment="当前状态(0:启用,1:禁用)")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=True, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=True, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
