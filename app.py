from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

# sqlite:///D:\Applications\python\flask-demo\app.db
db = SQLAlchemy(app)

from books.controllers import books
from auth.controllers import auth
app.register_blueprint(books)
app.register_blueprint(auth)

db.create_all()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'not found'})
