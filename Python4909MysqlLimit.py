from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)


# CREATE TABLE customer ( name varchar(255) , address varchar(255) ) 

# limit in db
# limit -> starting point 0,  no of elements -> 2 
query = " select * from customer limit 0, 2"

mycursor = mydb.cursor()
mycursor.execute(query)

for x in mycursor:
    print(x)
'''
('swayam', 'Agra Shastripuram')
('swayam', 'Agra Shastripuram')
'''


query = " select * from customer limit 2, 2"

mycursor = mydb.cursor()
mycursor.execute(query)

for x in mycursor:
    print(x)
'''
('karan', 'Agra ')
('xyz', 'mathura')
'''
