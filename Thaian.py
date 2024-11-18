import smtplib
import sqlite3
import yagmail

conn = sqlite3.connect("data/database.db")

cur = conn.cursor()

# username = input("Enter your username: ")
# email = input("Enter your email: ")
# password = input("Enter your password: ")

# cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)"
#             , (username,email,password))

conn.commit()
cur.close()


import yagmail
# Set up credentials
yag = yagmail.SMTP("buithaian321@gmail.com", "Buithaian321!")

# Send the email
yag.send(
    to="receiver_email@example.com",
    subject="Test Email",
    contents="Hello, this is a test email sent from Python!"
)

print("Email sent successfully!")
