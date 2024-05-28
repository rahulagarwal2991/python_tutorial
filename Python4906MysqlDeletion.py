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
query = "delete from customer where name = 'abc'"

mycursor = mydb.cursor()
mycursor.execute(query)

mydb.commit()

# this will delete all data
query = "delete from customer"

mycursor = mydb.cursor()
mycursor.execute(query)

mydb.commit()


