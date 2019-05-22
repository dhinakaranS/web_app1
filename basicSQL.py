# import mysql.connector

# mydb = mysql.connector.connect(
#   host="192.168.1.225",
#   user="root",
#   passwd="P@$$w0rd",
#   database = "python_db"
# )
# myCursor = mydb.cursor()


#create database
# createDatabaseQ = 'Create Database  python_db'
# myCursor.execute(createDatabaseQ)
# myCursor.execute('DESCRIBE users ')
# for x in myCursor:
#   print(x)

#create table
# createTab = 'create table  if not exists users (id binary(16), name varchar(20), phone int(10), city varchar(10), country varchar(10))'
# myCursor.execute(createTab)

#insert rows

# insert_users = 'insert into users (id,name,phone,city,country) values ("nubsfdcfs", "Kevin",48614226,"Chennai","India"), ("utosmsnfb", "Lara",4458521,"Virginia","USA")'
# myCursor.execute(insert_users)
# mydb.commit()

#update

# update_users = 'update users set name = "Surya" where name like "Karthik" '
# myCursor.execute (update_users)


#select

#delete rows

# del_users = 'delete  from users where name = "Enrique"'
# myCursor.execute(del_users)
# mydb.commit()
# myCursor.execute('select * from users ')
# for x in myCursor:
#   print(x)