from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)


# CREATE TABLE customer ( name varchar(255) , address varchar(255) ) 

# update an entry
query = "update customer set address = 'mathura' , name = 'xyz' where name = 'abc' "

mycursor = mydb.cursor()
mycursor.execute(query)

mydb.commit()

