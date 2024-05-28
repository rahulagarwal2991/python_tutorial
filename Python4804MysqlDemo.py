# brew install mysql
# pip uninstall mysql-connector
# pip3 uninstall mysql-connector
# pip3 install mysql-connector-python
#to start mysql.server start
from mysql import connector
# hostname, username , password , 
mydb = connector.connect(
    host="localhost",
    user="root",
    password=""
)