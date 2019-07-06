#文件站点相关flask+vue

/web vue 前端运行环境
1、首先安装node
2、然后安装进入web页面安装依赖包
# cd web && npm install
3、启动 npm run | npm run dev (开发模式)
前端vue启动完成 http://localhost:8080/

然后启动后台接口运行

1、安装python 依赖包 python 3
2、cd app && pip install 
3、安装执行环境 python setup.py install 
4、需要链接数据库，在 app/mysite/config.py 配置数据库
5、export FLASK_APP=server.py 
6、export FLASK_ENV=development
7、启动 flask run
启动的接口链接： http://127.0.0.1:5000/

都配置完成以后，(⊙o⊙)…，貌似完成了部署就可以直接访问了  http://localhost:8080/
