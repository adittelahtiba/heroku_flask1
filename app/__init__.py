from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

# time module
from datetime import datetime
from datetime import timedelta
from datetime import timezone

# jwt module
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# kafka
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookshelf"
mongo = PyMongo(app)
# bycrypt
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
app.config['JSON_SORT_KEYS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookshelf"
mongo = PyMongo(app)
# bycrypt
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
app.config['JSON_SORT_KEYS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# kafka event
TOPIC_NAME = "ADITYA-EMAILNA"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    api_version=(0, 11, 15)
)

@app.route('/',methods=['GET'])
def appawal():
    return {"aditya":"Pangestu"}

@app.route('/kafka', methods=['POST'])
def kafkaProducer():

    req = request.get_json()
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)
    # push data into INFERENCE TOPIC
    producer.send(TOPIC_NAME, json_payload)
    producer.flush()
    print("Sent to consumer")
    return jsonify({
        "message": "You will receive an email in a short while with the plot",
        "status": "Pass"})


# root
from app.books.route import *

