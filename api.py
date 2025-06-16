from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse, fields, marshal_with, abort, Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api= Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

user_args= reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="name is required")
user_args.add_argument('email', type=str, required=True, help="email is required")

userFields={
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String,
}

def __repr__(self):
    return f"user(name='{self.name}', email='{self.email}')"


class User(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def put(self):
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users,201

api.add_resource(User, '/api/user')
@app.route('/')
def home():
    return '<h1>Flask rest api</h1>'

if __name__ == '__main__':
    app.run(debug=True)