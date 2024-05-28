from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)

mycursor = mydb.cursor()

# create a table
mycursor.execute("CREATE TABLE customer ( name varchar(255) , address varchar(255) ) ")

# to show the tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# ('customer',)


