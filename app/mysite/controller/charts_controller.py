from flask import Blueprint, request, jsonify
from mysite import db, convert_to_json_string
from mysite.models.charts_model import Chartsmodel
import numpy as np, time
import pandas as pd
import json
from mysite.tools.tools import getNowDatetime, getPreDatetime


class ChartsController:

    def get_random_data(self):
        """
            获取随机一百条数据data
        :return:
        """
        frameData = np.random.rand(100,2)
        end = getNowDatetime()
        start = getPreDatetime(end, -10)
        dateTime = pd.date_range(start=str(start), periods=100, freq="100ms")
        dataTimeList = dateTime.values
        data = [list(item) + [str(dataTimeList[index])] for index, item in enumerate(frameData)]
        return data

    def save_charts_data(self, params):
        try:
            for item in params:
                print(item)
                price = round(float(item[0]), 8)
                volume = round(float(item[1]), 8)
                dateTime = item[2]
                addRow = Chartsmodel(price=price, volume=volume, dealTime=dateTime)
                db.session.add(addRow)
            db.session.commit()
            return True
        except:
            return False

    def get_charts_list(self):
        try:
            rows = Chartsmodel.query.order_by(Chartsmodel.id.desc()).limit(100).all()
            return convert_to_json_string(rows)
        except:
            return False
