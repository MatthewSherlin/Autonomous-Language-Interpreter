# sessions
from database import db, session_table
from flask import make_response
import mysql.connector
import os
import string
import random
import json
from flask import Flask, render_template_string, request, session, redirect, url_for

# ---------------session functions------------------------
def newSession():  # creates new session dic
    sessionId = newSessionId()
    s = {"session_id": sessionId, "user_id": ""}  # creating dic
    return s  # returning data


def getSession(request):
    sessionId = request.cookies.get(
        "session_id", default=None
    )  # asking for browser given data
    if sessionId == None:
        s = newSession()  # if none found create new
    else:  # if found, get it
        try:
            # s = read(sessionId)
            session = list(session_table.find(session_id=sessionId))
            sessionId = session[0].get("session_id")
            s = {"session_id": sessionId, "user_id": ""}
        except:  # exception for proctection
            s = newSession()
    return s  # return session
   # current_session = session['username']
    #return current_session


# saving session
def saveSession(response, session):
    assert type(session) is dict

    # updates the session with each save
    data = {"session_id": session["session_id"], "user_id": session["user_id"]}

    results = list(session_table.find(session_id=session["session_id"]))

    # if nothing is found a new session is inserted
    if results == []:

        session_table.insert(
            {"session_id": session["session_id"], "user_id": session["user_id"]}
        )
        response.set_cookie("session_id", session["session_id"], path="/")

    # else the session is updated
    else:
        session_table.update(data, ["session_id"])
        response.set_cookie("session_id", session["session_id"], path="/")


# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp


# uses token function to get new session ID
def newSessionId():
    return createToken()


# create token for session ID
def createToken(k=32):
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=k)
    )  # creates random string
