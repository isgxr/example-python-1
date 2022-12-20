#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'StarOS'

from flask import Flask


app = Flask(__name__)

# 请您来修正Hello, word的拼写错误吧！
# 请在修改完成后，通过主菜单 Git/Commit ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到Factory ( http://factory.staros.cloud/project/blueprint?id=last )，用同样的方法发布一个新实例即可看到修改后的效果。



@app.route('/')
def hello():
    return "copy-master分支。测试代码提交触发自动构建-2022-02-09。第一次提交是否触发了自动发布。2022-12-20 16：05.2022-12-20 16：07."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
