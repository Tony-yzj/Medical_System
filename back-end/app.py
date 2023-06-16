from flask import Flask, jsonify, json, request
from flask_cors import CORS
import json
import configparser
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from exts import db
import config
from model import *

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CORS(app)


with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs.fetchone())
        
def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

# 用户主页
@app.route('/api/index/money', methods=['POST','GET'])
def money():
    db.create_all() #创建所有表
    id=request.get_json('user_id')
    #print(id)
    column=PharmUser.query.filter_by(uid=id).first()
    #print(111)
    #print(column)
    if column==None:
        article = PharmUser(uid = id, asset= 0, pay= None, address= None)
        db.session.add(article)
        db.session.commit()
    # article = PharmUser(uid = 12345,asset= 0, pay= 'null', address= 'null')
    # #2提交操作
    # db.session.add(article)
    # db.session.commit()
    column=PharmUser.query.filter_by(uid=id)[0]
    print(column.asset)
    return jsonify(column.asset)
    #return jsonify(1000)

@app.route('/api/index/add', methods=['POST','GET'])
def add():
    db.create_all() #创建所有表
    data=request.get_json()
    id=data.get('id')
    column=PharmUser.query.filter_by(uid=id).first()
    if column==None:
        article = PharmUser(uid = id, asset= 0, pay= None, address= None)
        db.session.add(article)
        db.session.commit()
    funds=data.get('funds')
    m=data.get('m')
    print(id)
    article=PharmUser.query.filter_by(uid=id)[0]
    article.asset=article.asset+funds
    article.pay=m
    db.session.commit()
    print(article.asset)
    return jsonify(article.asset)

@app.route('/api/index/see', methods=['POST','GET'])
def table():
    db.create_all() #创建所有表
    # article = Order(uid = 12345, sum_price= 1000, address= '32舍159')
    # #2提交操作
    # db.session.add(article)
    # db.session.commit()
    id=request.get_json('user_id')
    table=[]
    users = Order.query.filter_by(uid=id).all()
    for user in users:
        table.append({
            'CODE': user.oid,
            'PRICE': user.sum_price,
            'ADDRESS': user.address,
            'COMMENT': user.comment,
            'DESCRIPTION': user.description

        })
    return jsonify(table)


# 医生管理药房
@app.route('/api/update', methods=['POST'])
@static_var('count', 1)
def update():
    # db.drop_all()
    data = request.get_json()
    name = data.get('name')
    tag = data.get('tag')
    num = int(data.get('num'))
    price = data.get('price')
    description = data.get('description')
    # 在这里处理表单数据
    medicine = Medicine(did=update.count,name=name, num=num, price=price, description=description,tag=tag)
    db.create_all()
    user = Medicine.query.filter_by(name=name).all()
    if user:
        user = user[0]
        print(user)
        user.num = int(user.num) + num
        user.tag = tag
        user.price = price
        user.description = description
        db.session.commit()
        return jsonify({'result': 'success'})
    else:
        update.count += 1
        db.session.add(medicine)
        db.session.commit()
        return jsonify({'result': 'success'})

@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    name = data.get('name')
    users = Medicine.query.filter_by(name=name).all()
    result = []
    for medicine in users:
        result.append({
            'did': medicine.did,
            'name': medicine.name,
            'price': medicine.price,
            'num': medicine.num,
            'tag': medicine.tag,
            'description': medicine.description
        })
    return jsonify(result)

# 用户获取药房信息
@app.route('/api/pharmacy/getData', methods=['GET', 'POST'])
def get_data():
    # db.drop_all()
    data_get = request.get_json()
    tag = data_get.get("tag")
    name = data_get.get("name")
    datas = Medicine.query.all()
    data = [{'did':data.did, 'name':data.name, 'price':data.price, 'num':data.num, 'tag':data.tag, 'description':data.description} for data in datas]
    
    res = list()
    for item in data:
        # print(item)
        if tag == '' or item["tag"] == tag:
            if name == '' or item["name"] == name:
                print(name)
                res.append(item)
    dic = {"items": res}

    print(dic)
    return jsonify(dic)

@app.route('/api/pharmacy/addCart', methods=['GET', 'POST'])
def addCart():
    data_get = request.get_json()
    uid = data_get.get("uid")
    did = data_get.get("did")
    
    num = data_get.get("shop")
    name = data_get.get("name")
    # print(num)
    price = data_get.get("price")
    # print(price)
    sum_price = price * num
    
    cart = Cart(did = did, num = num, sum_price = sum_price, uid = uid, name = name)
    
    db.create_all()
    db.session.add(cart)
    db.session.commit()
    
    # print(sum_price)
    return jsonify(sum_price)

@app.route('/api/pharmacy/getCart', methods=['GET', 'POST'])
def getCart():
    data = request.get_json()
    uid = data.get("uid")
    datas = Cart.query.filter_by(uid=uid).all()
    carts = [{'cid': data.cid, 'uid':data.uid, 'name':data.name, 'price':data.sum_price, 'num':data.num, 'oid' : data.oid, 'edit':False} for data in datas]
    res = list()
    for item in carts:
        if uid == item["uid"] and item["oid"] == -1:
            res.append(item)
        
    dic = {"items": res}
    return jsonify(dic)

@app.route('/api/pharmacy/deleteCart', methods=['GET', 'POST'])
def deleteCart():
    data = request.get_json()
    cid = data.get("cid")
    
    cart_to_del = Cart.query.filter_by(cid=cid).all()
    for item in cart_to_del:
        db.session.delete(item)
        
    db.session.commit()
    
    return 'delete success'

@app.route('/api/pharmacy/editCart', methods=['GET', 'POST'])
def editCart():
    data = request.get_json()
    cid = data.get("cid")
    num = int(data.get("num"))
    cart_to_edit = Cart.query.get(cid)
    if cart_to_edit:
        ori_s_price = int(cart_to_edit.sum_price)
        ori_num = int(cart_to_edit.num)
        price = ori_s_price / ori_num
        cart_to_edit.sum_price = num * price
        cart_to_edit.num = num
        print(price)
        print(num)
        db.session.commit()
        return {'message': 'Book updated successfully'}
    else:
        return {'error': 'Book not found'}
    
    
@app.route('/api/pharmacy/subForm', methods=['GET', 'POST'])
def subForm():
    db.create_all() #创建所有表
    data = request.get_json()
    uid = data.get("uid")
    sum = data.get("sum")
    print(sum)
    address = data.get("address")
    method = data.get("method")
    desc = data.get("desc")
    information = PharmUser.query.filter_by(uid=uid)[0]
    print(information.asset)
    if information.asset < sum:
        return jsonify(2)
    else:
        information.asset = information.asset - sum
        db.session.commit()
        column = Order(uid = uid, sum_price = sum, address = address, method = method, description = desc, comment = None)
        db.session.add(column)
        max_logins = db.session.query(func.max(Order.oid)).scalar()
        order = db.session.query(Order).filter(Order.oid == max_logins).all()
        oid = order[0].oid
        
        carts = db.session.query(Cart).filter(Cart.oid == -1).all()
        for item in carts:
            num = item.num
            did = item.did
            
            drug = db.session.query(Medicine).filter(Medicine.did == did).all()
            if drug[0].num < num:
                return jsonify(3)
            drug[0].num = drug[0].num - num    
                
            item.oid = oid

        db.session.commit()
        return jsonify(1)

    # 检查余额
    
    # 订单生成
    
    # 修改购物车
    
    
# 评论（组员未完成）
@app.route("/api/order/getOrders", methods=["GET","POST"])
def getOrders():
    # db.drop_all()
    data_get = request.get_json()
    uid=data_get.get("uid")
    datas = Order.query.all()
    data = [{"uid":data.uid,"oid":data.oid,"sum_price":data.sum_price,"method":data.method,"address":data.address,"description":data.description,"comment":data.comment} for data in datas]
    
    res = list()
    for order in data:
            if uid == '' or order["uid"] == int(uid) :
                print(uid)
                res.append(order)
    dic = {"orders": res}

    print(dic)
    return jsonify(dic)


@app.route("/api/order/AddComment", methods=["GET","POST"])
def AddComment():
    data=request.get_json()
    oid=data.get("oid")
    newcomment=data.get("comment")
    order_to_comment=Order.query.get(oid)
    if order_to_comment:
            order_to_comment.comment = newcomment
            db.session.commit()
            return jsonify({"msg": "评论成功"})

if __name__ == '__main__':
    app.run()