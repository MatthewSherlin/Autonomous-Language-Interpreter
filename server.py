from bottle import route, get, post 
from bottle import run, debug
from bottle import request, response, redirect, template
from bottle import default_app
from bottle import static_file
import mysql.connector

## connecting to database
## !!!may need to put root as password if no connection occurs!!!
## make sure database = ali ##

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ali"
    )



## Testing database connection ##
## create a table named test with username varchar(20), password varachar(20) to test connection 
#mycursor = db.cursor()

#mycursor.execute("INSERT INTO test (username, password) VALUES(%s,%s)", ("Test1","Test1"))
#db.commit()


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
