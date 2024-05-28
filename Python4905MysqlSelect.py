from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)


# CREATE TABLE customer ( name varchar(255) , address varchar(255) ) 
# selcting the data
query = "select * from customer"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()

# for x in result:
#     print(x)

'''
('Karan', 'Agra shaganj')
('swayam', 'Agra Shastripuram')
('swayam', 'Agra Shastripuram')
('swayam', 'Agra Shastripuram')
('karan', 'Agra ')
('abc', 'agra')
'''


# selecting particular columns

query = "select name from customer"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()

# for x in result:
#     print(x)

'''
('Karan',)
('swayam',)
('swayam',)
('swayam',)
('karan',)
('abc',)
'''
# select particular element
query = "select name from customer where name ='abc'"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()

# for x in result:
#     print(x)

# wild card selection
query = "select name from customer where name like '%y%'"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()

# for x in result:
#     print(x)

'''
('swayam',)
('swayam',)
('swayam',)
'''

# ORDER BY CLAUSE
# by default order by is in asc order
query = "select name from customer ORDER BY name desc"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()

for x in result:
    print(x)
