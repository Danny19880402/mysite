from mysite import db

class Chartsmodel(db.Model):
    __tablename__ = 'chart_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 支持事务操作和外键
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 价格
    price = db.Column(db.Float, doc='价格', nullable=False)
    # 数量
    volume = db.Column(db.Float, doc='数量', nullable=False)
    dealTime = db.Column(db.DateTime, doc='成交时间', nullable=False)

