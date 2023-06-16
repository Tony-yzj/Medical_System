from flask import Flask, jsonify, json, request
from flask_cors import CORS
import json
import configparser
import os
from flask_sqlalchemy import SQLAlchemy

# MySQL所在主机名
HOSTNAME = "127.0.0.1"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，自己设置
USERNAME = "root"
# 连接MySQL的密码，自己设置
PASSWORD = "c20011213j"
# MySQL上创建的数据库名称
DATABASE = "medicine"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    num = db.Column(db.Integer)
    price = db.Column(db.Float)
    description = db.Column(db.String(50))



def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@app.route('/api/update', methods=['POST'])
@static_var('count', 0)
def update():
    data = request.get_json()
    name = data.get('name')
    num = data.get('num')
    price = data.get('price')
    description = data.get('description')
    # 在这里处理表单数据
    user = User(id=update.count,name=name, num=num, price=price, description=description)
    db.create_all()
    update.count += 1
    db.session.add(user)
    db.session.commit()
    # 返回响应数据
    return jsonify({'result': 'success'})

@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    name = data.get('name')
    users = User.query.filter_by(name=name).all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'name': user.name,
            'price': user.price,
            'num': user.num,
            'description': user.description
        })
    return jsonify(result)


@app.route('/api/pharmacy/getData', methods=['GET', 'POST'])
def get_data():
    data = {
        "message": "Hello from Flask!",
        "items": [
            {
                "name": "阿莫西林",
                "DID": 1,
                "Num": 10,
                "Shop": 0,
                "Price": 100,
                "tag": '仅限医生',
                "Description": 'ahhh',
                "edit": False
            },
            {
                "name": "yahhh1",
                "DID": 1,
                "Num": 10,
                "Shop": 0,
                "Price": 100,
                "tag": '仅限医生',
                "Description": 'ahhh',
                "edit": False
            },
        ]
    }
    data_get = request.get_json()
    tag = data_get.get("tag")
    name = data_get.get("name")
    res = list()
    for item in data["items"]:
        # print(item)
        if tag == '' or item["tag"] == tag:
            if name == '' or item["name"] == name:
                print(name)
                res.append(item)
    dic = {"items": res}

    print(dic)
    return jsonify(dic)

if __name__ == '__main__':
    app.run()