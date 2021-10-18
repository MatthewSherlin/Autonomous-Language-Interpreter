# sessions
from database import db, session_table

import mysql.connector
import os
import string
import random
import json



# ---------------session functions------------------------
def newSession():  # creates new session dic
    sessionId = newSessionId()
    s = {"session_id": sessionId, "user_id": ""}  # creating dic
    return s  # returning data


def getSession(request):
    sessionId = request.get_cookie(
        "session_id", default=None
    )  # asking for browser given data
    if sessionId == None:
        s = newSession()  # if none found create new
    else:  # if found, get it
        try:
            # s = read(sessionId)
            session = list(session_table.find(session_id=sessionId))
            sessionId = session[0].get('session_id')
            s = {'session_id': sessionId, 'user_id': ""}
        except:  # exception for proctection
            s = newSession()
    return s  # return session


# saving session
def saveSession(response, session):
    assert type(session) is dict
    session_table.insert({'session_id': session['session_id'], 'user_id':session['user_id']})
    response.set_cookie('session_id', session['session_id'], path="/")  # sets session


# uses token function to get new session ID
def newSessionId():
    return createToken()


# create token for session ID
def createToken(k=32):
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=k)
    )  # creates random string

