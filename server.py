# ALI server file
##flask imports
from datetime import timedelta
from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

# from bottle import route, get, post
# from bottle import run, debug
# from bottle import request, response, redirect, template
# from bottle import default_app
# from bottle import static_file

from sessions import saveSession, getSession
from database import companies, saveUser, getUser

import hashlib
import os
import codecs

app = Flask(__name__)
app.secret_key = 'Ob,#1p{<y`|DZ!51c;_Y#|+u":{wwP'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/ali"
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Quiet warning message
app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"

db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

Session(app)
# db.create_all()

@app.before_request
def sessionTimeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=5)
    session.modified = True


# ----------------home page--------------------
@app.route("/home")
def homePage():
    print("SESSION USERNAME IS " + str(session.get("username")))
    if "username" not in session:
        return redirect("/")
    else:
        return render_template("home.html")


# -------------------login page functionality--------------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        # session = getSession(request)
        # this will grab user input from html page
        username = request.form["username"]
        password = request.form["password"]

        user = getUser(username)
        # print(type(user))  Debug prints
        # print(f"username is type: {type(username)}")
        # print(user)
        #!!we need to add a pop up if user credentials is wrong. Because we can not redirect to signup page
        # bootstrap has some cool alert messages
        if not user:
            return render_template(
                "login.html", failedLogin=True
            )  # if user not found, will redirect user back to login page
        if not verifyPassword(password, user["password"]):
            return render_template(
                "login.html", failedLogin=True
            )  # if password is wrong, will redirect to login page
        if username not in session:
            session["username"] = username  # adds username to session

        # saveSession(request.response, session)  # saves the session
        return redirect(
            "/home"
        )  # will redirect to home page with the user being logged in

    else:
        return render_template("login.html", failedLogin=False)


# ---------------sign up functionality ----------------
@app.route("/signup", methods=["GET", "POST"])
def signUpPage():
    if request.method == "POST":
        # session = getSession(request)  # get session
        companyKey = request.form["companyKey"]
        username = request.form["username"]  # get username form page
        print("Getting password")
        password = request.form["password"]  # get password from page
        print(f"password is: {password}")
        passwordRepeat = request.form["password_again"]  # get password from page

        if (
            password != passwordRepeat
        ):  # makes sure the double password input is the same
            # saveSession(request.response, session)
            # if "username" not in session:
                # session["username"] = username  ## saves the session using flask
                return render_template(
                    "signup.html", invalidCode=False, notPasswordMatch=True
                )  # will redirct to signup if not the same

        companyInfo = list(companies.find(company_key=companyKey))
        try:
            companyName = companyInfo[0].get("company_name")
        except:
            # need to return error code rather than redirect
            return render_template(
                "signup.html", invalidCode=True, notPasswordMatch=False
            )  # input message (bootstrap alert) that says company key wrong

        data = {  # saves user after signup
            "username": username,
            "password": generateCredentials(password),
            "company_name": companyName,  # change to company name
        }
        print(type(data))

        saveUser(data)
        if "username" not in session:
            session[
                "username"
            ] = username  # sets session user name to the new users name
        # saveSession(request.response, session)
        return redirect("/home")
    else:
        return render_template("signup.html", invalidCode=False, notPasswordMatch=False)


# --------------sign out function & route-----------------------
@app.route("/logout", methods=["GET"])
def getLogout():
    # session = getSession(request)  # get session
    # session["user_id"] = ""  # change session info to no user_id
    # saveSession(request.response, session)  # save session
    session.pop(
        "username", None
    )  # removes the user id from the session when they logout
    return redirect("/")  # redirect to login page


# ------------------------Credential functions---------------------
# function for hashing process
def bytesToString(byte):
    string = str(
        codecs.encode(byte, "hex"), "utf-8"
    )  # using utf-8 to change bytes to a string
    assert type(string) is str  # making sure its a string
    return string


# function for hashing process
def stringToBytes(string):
    byte = codecs.decode(bytes(string, "utf-8"), "hex")  # changing from string to bytes
    assert type(byte) is bytes  # making sure its bytes
    return byte


# The hashing function
def generateCredentials(Userpassword):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        "sha256",  # The hash digest algorithm for HMAC
        Userpassword.encode("utf-8"),  # Makes password byes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return {  # returns hash
        "salt": bytesToString(salt),
        "key": bytesToString(key),
    }


# passwords need to be verified. We need to hash and compare to see if its verifiable
def verifyPassword(Userpassword, Usercredentials):
    salt = stringToBytes(Usercredentials["salt"])  # get salt
    key = stringToBytes(Usercredentials["key"])  # get key

    newKey = hashlib.pbkdf2_hmac(  # process to hash the password to compare
        "sha256",  # The hash digest algorithm for HMAC
        Userpassword.encode("utf-8"),  # Convert the password to bytes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return newKey == key  # returns bool to see if they match


# for images on page
# @app.route("/static/png/<filename:re:.*\.png>")
# @app.route("/image/<filename:re:.*\.png>")
# def get_image(filename):
#     return app.send_static_file(filename=filename, root="static/images", mimetype="image/png")

# @app.route("/static/<filename:path>")
# def get_static(filename):
#     return app.send_static_file(filename=filename, root="static")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
