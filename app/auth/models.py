from app import db, ma, fields


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# class User(db.Model):
#     __tablename__ = "User"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     name = db.Column(db.String(100))
#     password = db.Column(db.String(100))
#     usertrans = db.relationship("Transaksi")

#     def __init__(self, username,name, password):
#         self.username = username
#         self.name = name
#         self.password = password

# class UserSchema(ma.Schema):
#     id = fields.Number(dump_only=True)
#     username= fields.String(required=True)
#     name= fields.String(required=True)
#     password = fields.Integer(required=True)
