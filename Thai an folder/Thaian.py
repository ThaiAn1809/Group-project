#important var!!!
app_password = "eibefqchnaqcamuf" #do not touch on this varible
#important var!!!

#IMPORT AREA:

import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#FUNCTION AREA:

#funtion insert Username-Email-Password to the database
def insert_u_e_p(username: str,email: str,password: str):
    """Function that inserts Username-Email-Password to the database.db

    Args:
        username (str): the user's useraname
        email (str): the user's email
        password (str): the user's password
    """

    #create connection and cursor:
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()

    #add the input data to the database.db file:
    cur.execute("INSERT INTO users(? ,? ,? ) VALUES(username,email,password)", (username,email,password))

    #commit and close:
    conn.commit()
    cur.close()



def send_email(sender_email: str,receiver_email: str,subject: str,body: str,app_password: str):

    # Set up the MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the body of the email
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

#input data:
username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter our password: ")

# Email credentials
sender_email = "tainambovien@gmail.com"
receiver_email = "buithaian321@gmail.com" #for example
subject = "Important email from TaskMaster app"
body = "Just testing:)))"

send_email(sender_email,receiver_email,subject,body,app_password)