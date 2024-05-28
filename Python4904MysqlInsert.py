from mysql import connector

# hostname, username , password , database
mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database= "form"
)

mycursor = mydb.cursor()
# CREATE TABLE customer ( name varchar(255) , address varchar(255) ) 
# create a table
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
values = ("swayam", "Agra Shastripuram")


mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, " record inserted")



# insert multiple enteries

sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
values = [
    ("swayam", "Agra Shastripuram"),
    ("karan", "Agra "),
    ("abc", "agra")
]


mycursor.executemany(sql, values)
mydb.commit()

print(mycursor.rowcount, " record inserted")
