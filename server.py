from bottle import route, get, post 
from bottle import run, debug
from bottle import request, response, redirect, template
from bottle import default_app
from bottle import static_file

@route("/")
def loginPage():
    return template("login")



#for images on page
@route("/static/png/<filename:re:.*\.png>")
@route("/image/<filename:re:.*\.png>")
def get_image(filename):
    return static_file(filename=filename, root="static/images", mimetype="image/png")

@route("/static/<filename:path>")
def get_static(filename):
    return static_file(filename=filename, root="static")

if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8080)
else:
    application = default_app()