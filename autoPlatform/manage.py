"""
@Author: hao.ling
@Date: 2020/11/6 14:09
@Annotation: 服务运行
"""
from autoPlatform.config.service import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9990, debug="debug")
