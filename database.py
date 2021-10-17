# database
import dataset

## connecting to database
## !!!may need to put root as password if no connection occurs!!!
## make sure database = ali ##

# Add your own password for localhost
password = None
db = dataset.connect(f'mysql://root:{password}@localhost/ali')


## Testing database connection ##
# Create a reference to table 'sessions'
session_table = db['sessions']

""" def createSessionTable():
    sql = "CREATE TABLE Sessions (session_id varchar(32), user_id int UNSIGNED)"
    myCursor.execute(sql)
 """

# myCursor.execute("CREATE TABLE test (username varchar(20), password varchar(20))")
# myCursor.execute("INSERT INTO test (username, password) VALUES(%s,%s)", ("Test1","Test1"))

session_table.insert(dict(session_id='session_id1234567891011121314151', user_id=123))
session_table.insert({'session_id':'session_id1234567891011121314180', 'user_id':189})

""" def insertInto(table, vals):
    sql = f"INSERT INTO {table} VALUES (%s, %s)"
    myCursor.executemany(sql, vals)
 """


#   Runs select statement using mysql.connector. 
""" def selectFrom(table, cols, where=None):
    if where == None:
        sql = f"SELECT {cols} FROM {table}"
    else:
        sql = f"SELECT {cols} FROM {table} WHERE {where}"
    myCursor.execute(sql)
 """

print(db.tables)
print(db['sessions'].columns)

row = db['sessions']
for row in db['sessions']:
    print(row)
""" def deleteFrom(table, val):
    sql = f"DELETE FROM {table} WHERE user_id = %s"
    myCursor.execute(sql, val)
 """
 
user = 123
s = list(session_table.find(user_id=user))
print(s[0].get('user_id'))
session = list(session_table.find(user_id=123))
print("session found with u_id = 123" , session)
print(len(session))
print(session[0].get('session_id'))
# createSessionTable()
vals = [
    ("session_id1234567891011121314151", 123),
    ("session_id1234567891011157314151", 124),
    ("session_id1234561491011121314151", 643),
    ("session_id1234567891083121314151", 129),
    ("session_id1234560091011121314151", 190),
    ("session_id1234567891017861314151", 906)
]
# insertInto("Sessions", vals)
# db.commit()

# Delete test record
session_table.delete(user_id=123)
print("record deleted")

for row in db['sessions']:
    print(row)

session_table.drop()
print("Sessions table dropped")

print(db.tables)

