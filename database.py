# database
import dataset

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


# Testing database setup
db["companies"].drop()

companies.insert(
    {
        "company_id": "1234",
        "company_name": "Avita",
        "company_key": "123thjmv79cdfj3ki5tye",
    }
)

#testing chart db
db["chart_table"].drop()
chart_table.insert({
    'username': 'dylan',
    'patient': 'Bob Dylan',
    'time' : '8:50 AM',
    'date' : "11/07/21",
    'notes': "back problem. cant sit up right. pain shoots down legs"

})

chart_table.insert({
    'username': 'dylan',
    'patient': 'Bob Marley',
    'time' : '10:50 AM',
    'date' : "11/08/21",
    'notes': "toe pain. cant walk. been going on for days now"

})

def getUser(username):
    try:
        user = list(users_table.find(username=username))
        username = user[0].get("username")
        password = user[0].get("password")
        company = user[0].get("company_name")
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
            "company_name": data["company_name"],
        }
    )
    return
