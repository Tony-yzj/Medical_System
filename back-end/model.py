from exts import db

# 创建数据库模型类
# 公用用户数据表，按照整合的来就行


# 药房私用数据库
class Medicine(db.Model):
    __tablename__ = 'pharmacy'
    did = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    num = db.Column(db.Integer)
    price = db.Column(db.Float)
    tag = db.Column(db.String(50))
    description = db.Column(db.String(50))

# # 药房内存储信息数据表
class PharmUser(db.Model):
    __tablename__ = 'pharm_user'
    uid = db.Column(db.Integer, primary_key=True)
    asset = db.Column(db.Float)
    address = db.Column(db.String(128))
    pay = db.Column(db.String(128))
    
# 购物车信息存储表
class Cart(db.Model):
    __tablename__ = 'pharm_cart'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer)
    did = db.Column(db.Integer)
    num = db.Column(db.Integer)
    name = db.Column(db.String(50))
    sum_price = db.Column(db.Float)
    oid = db.Column(db.Integer, default='-1')

# 订单表（用于评价）
class Order(db.Model):
    __tablename__ = 'pharm_order'
    uid = db.Column(db.Integer)
    oid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sum_price = db.Column(db.Float)
    method = db.Column(db.String(32)) #取药方式
    comment = db.Column(db.String(128))
    address = db.Column(db.String(128))
    description = db.Column(db.String(128))
