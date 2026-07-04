from Database import execute_query,conn
import pandas as pd
import mysql.connector
import sys

global logged_in_user
logged_in_user = None


def dashboard():
    pass


def login():
    username = input("Enter Username : ")
    ps = input("Enter Password : ")
    query = """Select * from information where user_name LIKE '{}' and pass LIKE '{}' """.format(username,ps)
    try :
        execute_query(conn,query)
    except:
        print("Could not log in")
    else:
        logged_in_user = username 
        print(username)


def new_user():
    username = input("Enter Username : ")
    id = int(input("Enter id : "))
    email = input("Enter Email : ")
    ps = input("Enter Password : ")

    query = """Insert into information (user_name , id , email , pass) values ('{}','{}','{}','{}')""".format(username,id,email,ps)
    execute_query(conn,query)

while True:
    if(logged_in_user==None) :
        print("1.Login into Application")
        print("2.Register [New User!!]")
        print("3.Exit ")
        a = int(input("Enter Your Choice : "))

        if a==1:
            login()
        elif a==2:
            new_user()
        else:
            sys.exit()

