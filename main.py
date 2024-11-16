# Chating place:

# ...

# Importing place:

import math
import random
import sqlite3
import numpy
import requests 


# Defining class place:

# ... 

# Defining function place:

# ...

if __name__ == "__main__":
    # define connection and cursor:
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # adding names, password and email:
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # email and password list
    email_list = []
    password_list = []
    
    #fetch the email and password from the users table
        
    cur.execute("SELECT email, password FROM users")
    rows = cur.fetchall()
    
    for row in rows:
        email_data, password_data = row
        email_list.append(email_data)
        password_list.append(password_data)
        
    
    # insert values for username, email and password:
    if email not in email_list:
        if password not in password_list:
            cur.execute(f"""INSERT INTO users(username, email, password)
                        VALUES (?, ?, ?)""", (username,email,password))
        else:
            print("INVAILD password")
    else:
        print("INVAILD email")
        

    # commit and close the connection:
    conn.commit()
    conn.close()