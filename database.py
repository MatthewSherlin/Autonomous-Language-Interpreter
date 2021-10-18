# database
import dataset

## connecting to database
## !!!may need to put root as password if no connection occurs!!!
## make sure database = ali ##

# Add your own password for localhost
db = dataset.connect('mysql://root:password@localhost/ali')
# companies = db.get_table('companies')



## Testing database connection ##
# Create a reference to table 'sessions'
session_table = db['sessions']
users_table = db['users_table']
companies = db['companies']


# Testing database setup 
db['companies'].drop()

companies.insert(
    {'company_id':'1234' ,
    'company_name': 'Avita',
    'company_key': '123thjmv79cdfj3ki5tye'}
)
""" session_table.insert(dict(session_id='session_id1234567891011121314151', user_id=123))
session_table.insert({'session_id': 'session_id1234567891011121314180', 'user_id':189})



print(db.tables)
print(db['sessions'].columns)

row = db['sessions']
for row in db['sessions']:
    print(row) 
user = 123
s = list(session_table.find(user_id=user))
print(s[0].get('user_id'))
session = list(session_table.find(user_id=123))
print("session found with u_id = 123" , session)
print(len(session))
print(session[0].get('session_id'))


# Delete test record
session_table.delete(user_id=123)
print("record deleted")

for row in db['sessions']:
    print(row)

session_table.drop()
print("Sessions table dropped")

print(db.tables)
 """
####



def getUser(username):
    try:
        user = list(users_table.find(username = username))
        username = user[0].get('username')
        password = user[0].get('password')
        company = user[0].get('company_name')
        data = {'username': username, 'password': password, 'company_name':company}
        return data
    except:
        return None
    

def saveUser(data):
    assert type(data) is dict
    users_table.insert(
    {'username': data['username'],
     'password': data['password'], 
     'company_name': data['company_name'], 
     'user_id' : data['user_id']}
    )
    return 
