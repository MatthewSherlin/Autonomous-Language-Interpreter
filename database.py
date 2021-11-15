# database
import dataset

import datetime
import hashlib
import os
import codecs

import string
import random
## connecting to database
## !!!may need to put root as password if no connection occurs!!!
## make sure database = ali ##

# Add your own password for localhost
db = dataset.connect("mysql://root:@localhost/ali")

## Testing database connection ##
# Create a reference to table 'sessions'
users_table = db["users_table"]
companies = db["companies"]
chart_table = db["chart_table"]
sessions = db["sessions"]

## 
def companyIdGenerator(size=4, uchars=string.digits):
    return ''.join(random.choice(uchars) for _ in range(size))

# Testing database setup
db["companies"].drop()

companies.insert(
    {
        "company_id": "0001",
        "company_name": "ALI",
        "company_key": "123thjmv79cdfj3ki5tye",
    }
)

#testing chart db
db["chart_table"].drop()
chart_table.insert({
    'username': 'dylan',
    'patient': 'Bob Dylan',
    'time_stamp' : '2021-11-12 17:32:11',
    'notes': "back problem. cant sit up right. pain shoots down legs"

})

chart_table.insert({
    'username': 'dylan',
    'patient': 'Bob Marley',
    'time_stamp' : '2021-11-11 17:32:11',
    'notes': "toe pain. cant walk. been going on for days now"

})

currentTimeStamp = datetime.datetime.now()

chart_table.insert({
    'username': 'dylan',
    'patient': 'Randy Marsh',
    'time_stamp' : str(currentTimeStamp),
    'notes': "ate too much mcribs"

})

def getUser(username):
    try:
        user = list(users_table.find(username=username))
        username = user[0].get("username")
        password = user[0].get("password")
        company = user[0].get("company_name")
        isAdmin = user[0].get("is_admin")
        data = {"username": username, "password": password, "company_name": company}
        return data
    except:
        data = {"username": '', "password": '', "company_name": ''}
        return data


def saveUser(data):
    assert type(data) is dict
    users_table.insert(
        {
            "username": data["username"],
            "password": data["password"],
            "company_name": data["company_name"]
        }
    )
    return

def saveCompany(data):
    assert type(data) is dict
    #try:
    #companies.find(company_key = data["company_key"])
    #except:
    companies.insert(
        {
            "company_id": data["company_id"],
            "company_name": data["company_name"],
            "company_key": data["company_key"]
        }
    )
    return

def isAdmin(username):
    if username  == "admin":
        return True
    else: 
        return False



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


def generateCredentials(Userpassword):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        "sha256",  # The hash digest algorithm for HMAC
        Userpassword.encode("utf-8"),  # Makes password byes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
    )

    return '{"salt": "' + str(bytesToString(salt)) + '", "key": "' + str(bytesToString(key)) + '"}'

