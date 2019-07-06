from datetime import datetime, date, timedelta
import time

def getNowDatetime():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dt = datetime.strptime(str(t), '%Y-%m-%d %H:%M:%S')
    return dt

def getPreDatetime(dateTime, secs=-10):
    pre_time = dateTime + timedelta(seconds=int(secs))  # 减去10s
    return pre_time