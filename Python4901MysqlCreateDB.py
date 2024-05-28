# brew install mysql
# pip uninstall mysql-connector
# pip3 uninstall mysql-connector
# pip3 install mysql-connector-python
#to start mysql.server start

'''
database create
table create
Inside table CRUD operation
Create 
Read
Update
Delete
Mysql extra queries , order by, where clause...
mysql terminal : mysql -u root -p
show databases;
use form;
'''

from mysql import connector

# hostname, username , password , 
mydb = connector.connect(
    host="localhost",
    user="root",
    password=""
)


mycursor = mydb.cursor()
# create a database
# mycursor.execute("CREATE DATABASE form")

# show listing of DB
# mycursor.execute("show databases")

# for x in mycursor:
#     print(x)


