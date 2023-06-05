
import mysql.connector
from mysql.connector import Error

from tabulate import tabulate

user_db_con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="EllaiDhurai007",
    database="user"
)

if user_db_con:
    print("connected")
else:
    print("connection error")

def create(name, age, city):
    req = user_db_con.cursor()
    sql ="insert into userdata(NAME,AGE,CITY) values(%s,%s,%s);" # %s-string for pass dyanmic input
    user=(name,age,city) # the value in this variable is automatically assigned to %s 
    req.execute(sql,user) 
    user_db_con.commit() # to commit changes in sql
    print("data insert success")

def read():
    req = user_db_con.cursor() # cursor is temporary connection to database when we make request
    sql = "select ID,NAME,AGE,CITY from userdata" # sql query
    req.execute(sql)
    # result = req.fetchone()
    # result = req.fetchmany()
    result = req.fetchall()

    print(tabulate(result,headers=['ID','NAME','AGE','CITY']))

def update(id,name, age, city):
    req = user_db_con.cursor()
    sql ="update userdata SET name=%s,age=%s,city=%s where id=%s" # %s-string for pass dyanmic input
    user=(id,name,age,city) # the value in this variable is automatically assigned to %s 
    req.execute(sql,user) 
    user_db_con.commit() # to commit changes in sql
    print("data update success")

def delete(id):
    req = user_db_con.cursor()
    sql ="delete from userdata where id=%s" # %s-string for pass dyanmic input
    user=(id,) # to pass single value we also need to put comma at end  
    req.execute(sql,user) 
    user_db_con.commit() # to commit changes in sql
    print("data delete success")

while True:
    print("1.create")
    print("2.read")
    print("3.update")
    print("4.delete")
    print("5.exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        name = input("name: ")
        age = input("age: ")
        city = input("city: ")
        create(name, age, city)

    elif choice == 2:
        read()

    elif choice == 3:
        id = input("id: ")
        name = input("name: ")
        age = input("age: ")
        city = input("city: ")
        update(name, age, city,id) 

    elif choice == 4:
      id = input("enter the id: ")
      delete(id)

    elif choice == 5:
      quit()

    else:
      print("please select correct option")