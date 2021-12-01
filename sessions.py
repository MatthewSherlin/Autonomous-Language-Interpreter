# sessions
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'Ob,#1p{<y`|DZ!51c;_Y#|+u":{wwP'

# configure flask app for server-side sessions
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/ali"
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Quiet warning message
app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"

db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

Session(app)
db.create_all()

# functionality for session timeout
@app.before_request
def sessionTimeout():
    session.permanent = True # so session persists even if browser is closed
    app.permanent_session_lifetime = timedelta(minutes=20) # session expires after 20 mins
    session.modified = True

