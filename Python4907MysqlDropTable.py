from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)


# CREATE TABLE customer ( name varchar(255) , address varchar(255) ) 
# deletion of an entry
# query = "DROP TABLE customer"

# mycursor = mydb.cursor()
# mycursor.execute(query)


query = "DROP TABLE IF EXISTS customer"

mycursor = mydb.cursor()
mycursor.execute(query)
