#important var!!!
app_password = "eibefqchnaqcamuf" #do not touch on this varible
#important var!!!

import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#create connection and cursor:
conn = sqlite3.connect("data/database.db")
cur = conn.cursor()

#input data:
username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter our password: ")

#add the input data to the database.db file:
cur.execute("INSERT INTO users VALUES(username,email,password)", (username,email,password))

#commit and close:
conn.commit()
cur.close()



# Email credentials
sender_email = "tainambovien@gmail.com"
receiver_email = "buithaian321@gmail.com"

# Set up the MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email using App Password"

# Add the body of the email
body = "Hello, this email is sent using an App Password."
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)  # Login using App Password
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")
