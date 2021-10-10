from bottle import route, get, post 
from bottle import run, debug
from bottle import request, response, redirect, template
from bottle import default_app

@route("/")
def loginPage():
    return template("login")



if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
else:
    application = default_app()