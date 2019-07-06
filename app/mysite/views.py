# -*- coding: UTF-8 -*-
from flask import Flask,render_template,jsonify,request,g, url_for,abort
from mysite import app
from mysite.models import *
import hashlib
from mysite.controller.charts_controller import ChartsController
import json

from mysite.view.charts_views import charts
#注册蓝图 接口
app.register_blueprint(charts)



@app.route("/api/charts", methods=['GET', 'POST'])
def home():
    chartC = ChartsController()
    charts_data = chartC.get_random_data()
    resp = jsonify({'code': '0', 'msg': 'success', 'data': charts_data})
    # 不建议头部设置跨域访问，生产环境使用nginx反向代理前后端域名解决跨域问题
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'HEAD, OPTIONS, GET, POST, DELETE, PUT'
    return resp

@app.route("/api/addCharts", methods=['POST'])
def saveCharts():
    chartsData = request.form.get('chartsData')
    chartC = ChartsController()
    result = chartC.save_charts_data(json.loads(chartsData))
    if result:
        resp = jsonify({'code': '0', 'msg': 'success', 'data': []})
        # 不建议头部设置跨域访问，生产环境使用nginx反向代理前后端域名解决跨域问题
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'HEAD, OPTIONS, GET, POST, DELETE, PUT'
        return resp
    else:
        abort(500)

@app.route("/api/chartsList", methods=['get'])
def getChartsList():
    chartC = ChartsController()
    result = chartC.get_charts_list()
    resp = jsonify({'code': '0', 'msg': 'success', 'data': json.loads(result)})
    # 不建议头部设置跨域访问，生产环境使用nginx反向代理前后端域名解决跨域问题
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'HEAD, OPTIONS, GET, POST, DELETE, PUT'
    return resp



