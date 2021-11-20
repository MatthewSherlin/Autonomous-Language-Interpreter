# ALI server file
# Flask imports
from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import session
from flask import Response

from database import companies, saveUser, getUser, chart_table,isAdmin, db
from database import generateCredentials, stringToBytes, companyIdGenerator, saveCompany
from sessions import app
from translatetext import takeHomeTranslate, clearTextTags,clearHomeTags

import hashlib
import datetime
import time
import threading
import toget
import math
import random



# ----------------home page--------------------
@app.route("/home", methods=["GET", "POST"])
def homePage():
    
    if request.method == 'POST':
        patientName = request.form["name"]
        userNotes = request.form["notes"]
        highlights = request.form["highlights"]
        dateAndTime = str(datetime.datetime.now())
        date = dateAndTime[0:10]
        time = dateAndTime[11:19]
        username = session.get("username")
        
        try:
            chart_table.insert({
                'username': username,
                'patient': patientName,
                'time' : time,
                'date' : date,
                'notes': userNotes,
                'time_stamp': dateAndTime,
                'highlights': highlights
            })
            
        except Exception as e:
            return Response(e, status=409)
        
        if session.get("username")  == "admin":
            return render_template("home.html", isAdmin = True)

        elif "username" not in session:
            return redirect("/")
        else:
            return render_template("home.html", isAdmin = False)
        
    else:
       ## clearHomeTags() may need to uncomment!!
        if session.get("username") == "admin":
            return render_template("home.html", isAdmin = True)

        elif "username" not in session:
            return redirect("/")
        else:
            return render_template("home.html", isAdmin = False)


# -------------------translate---------------------------------
@app.route("/translate", methods=["GET", "POST"])
def dynamic_page():
    if request.method == "POST":
        languageOne = request.form["languages1"]
        langaugeTwo = request.form["languages2"]

        if languageOne and langaugeTwo:
            toget.main(languageOne, langaugeTwo)
            return render_template("home.html", isAdmin = True) if session.get("username") == "admin" else render_template("home.html", isAdmin = False)
        else:
            return render_template("home.html", isAdmin = True, values = False) if session.get("username") == "admin" else render_template("home.html", isAdmin = False, values=False)

    else:
        return render_template("home.html", isAdmin == True) if session.get("username") == "admin" else render_template("home.html", isAdmin = False)
    

# -------------------login page functionality--------------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def loginPage():

    if request.method == "POST":
        # this will grab user input from html page
        username = request.form["username"]
        password = request.form["password"]

        user = getUser(username) #type dict

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

            if(isAdmin(username)):
                 print("ADMIN FOUND")  ## checks if user is admin
                 return render_template("home.html",isAdmin = True)  # will redirect to home page with the user being logged in
            else:
                 return render_template("home.html",isAdmin = False)  



    else:
        return render_template("login.html", failedLogin=False)


# ---------------sign up functionality ----------------
@app.route("/signup", methods=["GET", "POST"])
def signUpPage():
    
    if request.method == "POST":
        companyKey = request.form["companyKey"]
        username = request.form["username"]  # get username form page
        print("Getting password")
        password = request.form["password"]  # get password from page
        print(f"password is: {password}")
        passwordRepeat = request.form["password_again"]  # get password from page

        # checking to see if username is already taken
        oldUser = getUser(username)
        oldName = str(oldUser["username"])

        if oldName.upper() == username.upper():
            # username has been taken
            return render_template(
                "signup.html",
                invalidCode=False,
                notPasswordMatch=False,
                badUsername=True,
            )

        if (
            password != passwordRepeat
        ):  # makes sure the double password input is the same
            if "username" not in session:
                session["username"] = username  ## saves the session using flask
                return render_template(
                    "signup.html",
                    invalidCode=False,
                    notPasswordMatch=True,
                    badUsername=False,
                )  # will redirct to signup page if not the same

        companyInfo = list(companies.find(company_key=companyKey))
        try:
            companyName = companyInfo[0].get("company_name")
        except:
            # need to return error code rather than redirect
            return render_template(
                "signup.html",
                invalidCode=True,
                notPasswordMatch=False,
                badUsername=False,
            )  # input message (bootstrap alert) that says company key wrong

        data = {  # saves user after signup
            "username": username,
            "password": generateCredentials(password),
            "company_name": companyName,  # change to company name
        } # data is type dict
        print(type(data))

        
        saveUser(data)
      
        if "username" not in session:
            session["username"] = username  
            # sets session user name to the new users name
        return redirect("/")
    else:
        return render_template(
            "signup.html", invalidCode=False, notPasswordMatch=False, badUsername=False
        )



# --------------sign out function & route-----------------------
@app.route("/logout", methods=["GET"])
def getLogout():
    clearHomeTags()
    session.pop(
        "username", None
    )  # removes the user id from the session when they logout
    return redirect("/")  # redirect to login page


##takeHomeTranslate(var1)
# ---------Translation page --------------
@app.route("/takehome", methods=["GET", "POST"])
def takeHome():
    clearTextTags()
    if request.method == "POST":
        langaugeTwo = request.form["languages2"]
        text        = request.form["t1"]

        if langaugeTwo:
            takeHomeTranslate(langaugeTwo, text)
            return render_template("takeHome.html", isAdmin = True) if session.get("username") == "admin" else render_template("takeHome.html", isAdmin = False)    
        else:
            return render_template("takeHome.html", isAdmin = True, values = False) if session.get("username") == "admin" else render_template("takeHome.html", isAdmin = False, values = False)    
                 
    else:
        return render_template("takeHome.html", isAdmin = True) if session.get("username") == "admin" else render_template("takeHome.html", isAdmin = False)


#------------admin create keys page--------------------
@app.route("/admin", methods=["GET", "POST"])
def getAdmin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        companyName = request.form["companyName"]
        companyKey = request.form['companyKey']
       

        user = getUser(username)

        if username != "admin":
            return render_template("admin.html", failedLogin = True, isAdmin = True, keyMade = False)
        if not verifyPassword(password, user["password"]):
            return render_template("admin.html", failedLogin = True, isAdmin = True, keyMade = False)

        key = generateKey(20)
        
        companyID = companyIdGenerator()
        data = {
            "company_id": companyID,
            "company_name": companyName,
            "company_key": key,
        }
        
        saveCompany(data)
        return render_template("admin.html", failedLogin = False, isAdmin = True, keyMade = True, key = key)   
    else:
        return render_template("admin.html", failedLogin = False, isAdmin = True, keyMade = False)



# -------chart Page -----------------
@app.route("/mychart")
def getChart():
    username = session.get("username")
    itemsInChart = chart_table.find()
    itemsInChart = [ dict(x) for x in list(itemsInChart) if x['username'] == username ]
    if session.get("username") == "admin":
        return render_template("chart.html", itemsInChart = itemsInChart,isAdmin = True)
    else:
       return render_template("chart.html", itemsInChart = itemsInChart,isAdmin = False) 




# passwords need to be verified. We need to hash and compare to see if its verifiable
def verifyPassword(Userpassword, Usercredentials):
    
    if type(Usercredentials) == str:
        salt = stringToBytes(Usercredentials[10:74])
        key = stringToBytes(Usercredentials[85:149])
    else:
        salt = stringToBytes(Usercredentials["salt"])  # get salt
        key = stringToBytes(Usercredentials["key"])  # get key

    newKey = hashlib.pbkdf2_hmac(  # process to hash the password to compare
        "sha256",  # The hash digest algorithm for HMAC
        Userpassword.encode("utf-8"),  # Convert the password to bytes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return newKey == key  # returns bool to see if they match

##runs in the backgroud and deletes records that are 24 hours old
def background():
    minutes = 0
 
    while True:

            #print("minutes " + str(minutes))
            ##if an hour has passed
            if minutes > 60:
                try:
                    db.query('DELETE FROM chart_table WHERE time_stamp<=DATE_SUB(NOW(), INTERVAL 1 DAY);')
                    db.commit()
                    minutes = 0
                    #currentTimeStamp = datetime.datetime.now()
                    #print("CURRENT TIME STAP " + str(currentTimeStamp))

                except: pass
            time.sleep(60)
            minutes = minutes + 1
    

def generateKey(length):
    result           = ''
    characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for i in range(length):
      result += characters[math.floor(random.randint(0, len(characters)-1))]
      
    return result
   

if __name__ == "__main__":
 
    b = threading.Thread(name='background', target=background)

    b.daemon = True
    b.start()
    app.run(host="localhost", port=8080, debug=True)









