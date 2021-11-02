# database
import dataset

## connecting to database
## !!!may need to put root as password if no connection occurs!!!
## make sure database = ali ##

# Add your own password for localhost
db = dataset.connect('mysql://root:db_password@localhost/ali')

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
