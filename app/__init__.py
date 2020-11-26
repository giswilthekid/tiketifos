from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ljznsxli:d2Z7FPap1LZEUzC2d-opcI1ttZMkdGL1@suleiman.db.elephantsql.com:5432/ljznsxli'
db = SQLAlchemy(app)

from app.models import User, Tiket
from app import routes