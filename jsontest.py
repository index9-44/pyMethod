#!/usr/bin/python
# -*- coding: UTF-8 -*-


#本模块主要测试于使用flask框架进行相关接口开发。

import requests
#Flask 模块：Flask 框架的核心模块，提供了创建 Web 应用程序的基础功能。
# jsonify 模块：将 Python 字典或列表等数据类型转换成 JSON 格式的模块。
# request 模块：用于获取 HTTP 请求中的数据，如请求参数、请求头、请求体等等。
from flask import Flask, jsonify, request
#创建实例
app = Flask(__name__)
@app.route('/api/data', methods=['POST'])
@app.route('/api/data', methods=['GET'])

#post接口
def post_data():
    # 获取客户端请求中的参数
    data = request.json

    # 假设有一个数据字典
    allowed_keys = ['name', 'age', 'city']
    filtered_data = {k: v for k, v in data.items() if k in allowed_keys}

    # 返回过滤后的数据字典
    return jsonify(filtered_data)
#get接口
def get_data():
    url = request.args.get('key')  # 获取 url 参数
    data={'url:':url}
    return jsonify(data)  # 返回 JSON 格式数据

if __name__ == '__main__':
    # print("hello world")
    app.run(debug=True)