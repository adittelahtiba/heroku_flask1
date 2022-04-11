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
    title = request.json['title']
    author = request.json['author']
    stock = request.json['stock']
    data = {'code': code, 'title': title, 'author': author, 'stock': stock}
    new_books = mongo.db.books.insert_one(data)
    return jsonify({"new_book": True})


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
    return result.raw_result


@app.route('/book', methods=['DELETE'])
# @jwt_required()
def delete_book():
    code = request.json['code']
    book = mongo.db.books.delete_one({'code': code})
    return book.raw_result
