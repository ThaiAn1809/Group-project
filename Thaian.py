import sqlite3

conn = sqlite3.connect("data/database.db")

cur = conn.cursor()

username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter our password: ")

cur.execute("INSERT INTO users VALUES(username,email,password)", (username,email,password))

conn.commit()
cur.close()