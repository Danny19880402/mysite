# -*- coding: UTF-8 -*-
from mysite import app


if __name__ == '__main__':
    '''
    开启 debug模式
    # 设置 host='0.0.0.0'，让操作系统监听所有公网 IP
    '''
    app.run(debug=True, host="127.0.0.1", port="5000")
    # mysite.run(debug=True)