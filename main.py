# Chating place:

# ...

# Importing place:

import math
import random
import sqlite3
import numpy


# Defining class place:

# ... 

# Defining function place:

# ...

if __name__ == "__main__":
    # define connection and cursor:
    conn = sqlite3.connect("/data/database.db")
    cur = conn.cursor()

    # adding names, password and email:
    username = input("Enter your username: ")
    email = input("Enter your password: ")
    password = input("Enter your password: ")
    cur.execute(f"INSERT INTO users(username, email, password) VALUES ({username}, {email}, {password}) ")