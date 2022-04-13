from unittest import result
from app import app, mongo, jsonify, request
from flask_jwt_extended import jwt_required
from pymongo.errors import BulkWriteError


@app.route('/books', methods=['GET'])
# @jwt_required()
def index_books():
    data = mongo.db.books.find()
    aData = [{"code": row['code'], "title": row['title'],
              "author":row['author'], "stock":row['stock']} for row in data]
    return jsonify(aData)


@app.route('/book', methods=['POST'])
# @jwt_required()
def create_book():
    code = request.json['code']
    duplikat = mongo.db.books.find_one({"code":code})
    if duplikat:
        return {'new_book':False,'message':'Book code has been used'},400
    title = request.json['title']
    author = request.json['author']
    stock = request.json['stock']
    data = {'code': code, 'title': title, 'author': author, 'stock': stock}
    result = mongo.db.books.insert_one(data)
    return jsonify({"result": result.acknowledged})


@app.route('/book', methods=['PUT'])
# @jwt_required()
def update_book():
    code = request.json['code']
    title = request.json['title']
    author = request.json['author']
    stock = request.json['stock']
    data = {'title': title, 'author': author, 'stock': stock}
    result = mongo.db.books.update_one(
        {'code': code}, {"$set": data})
    return {'result':result.acknowledged,'matched_count':result.matched_count,'modified_count':result.modified_count}


@app.route('/book', methods=['DELETE'])
# @jwt_required()
def delete_book():
    code = request.json['code']
    result = mongo.db.books.delete_one({'code': code})
    return {'result':result.acknowledged,'delete_count':result.deleted_count}
