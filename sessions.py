# sessions
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'Ob,#1p{<y`|DZ!51c;_Y#|+u":{wwP'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/ali"
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Quiet warning message
app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"

db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

Session(app)
#db.create_all()

@app.before_request
def sessionTimeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)
    session.modified = True

