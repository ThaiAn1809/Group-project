# important var!!!
app_password = "fimhhmpykyoyaxuc"  # do not touch on this varible
# important var!!!

# IMPORT AREA:

import sqlite3
import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CLASS EXCEPTION AREA:


class InvaildEmail(Exception):
    """a custom exception name InvaildEmail

    Args:
        Exception (type): the Exception class
    """

    def __init__(self, email, message="Invaild email"):
        self.mesage = message
        self.email = email
        super().__init__(f"{message}: {email}")


class InvaildPassword(Exception):
    """a custom exception name InvaildPassword

    Args:
        Exception (type): the Exception class
    """

    def __init__(self, password, message="Invaild password"):
        self.mesage = message
        self.email = password
        super().__init__(f"{message}: {password}")


# CLASS AREA:


class Email:
    """a email type

    Raises:
        InvaildEmail: raise this if the email is invaild

    """

    EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def __init__(self, address: str):
        self.address = address
        if not self.is_valid():
            raise InvaildEmail(address)

    def is_valid(self) -> bool:
        return re.match(self.EMAIL_REGEX, self.address) is not None


class Password:
    """a password type

    Raises:
        InvaildPassword: raise this if the email is invaild

    """

    def __init__(self, password: str):
        self.password = password
        if not self.is_valid():
            raise InvaildPassword(password)

    def is_valid(self) -> bool:
        self.__alphabet = [
            "a",
            "b",
            "c",
            "d",
            "r",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        self.__upper_alphabet = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "I",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.__symbols = [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "<",
            ">",
            "?",
            ":",
            "{",
            "}",
            "[]",
            "-",
            "_",
            "=",
            "+",
            ".",
            "/",
            "'",
            ";",
            "",
        ]
        return (
            (self.__alphabet in self.password)
            and (self.__upper_alphabet in self.password)
            and (self.__symbols in self.password) is not None
        )


# FUNCTION AREA:


def insert_u_e_p(username: str, email: str, password: str):
    """Function that inserts Username-Email-Password to the database.db

    Args:
        username (str): the user's useraname
        email (str): the user's email
        password (str): the user's password
    """

    # create connection and cursor:
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()

    # add the input data to the database.db file:
    cur.execute(
        "INSERT INTO users(? ,? ,? ) VALUES(username,email,password)",
        (username, email, password),
    )

    # commit and close:
    conn.commit()
    cur.close()


def send_email(
    sender_email: str, receiver_email: str, subject: str, body: str, app_password: str
):
    """send an email

    Args:
        sender_email (str): the sender email
        receiver_email (str): the receiver_email
        subject (str): the subject of the email
        body (str): the body of the email
        app_password (str): :)
    """
    # Set up the MIME message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add the body of the email
    msg.attach(MIMEText(body, "plain"))

    # Set up the SMTP server
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)  # Login using App Password
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


conn = sqlite3.connect("data/database.db")
cur = conn.cursor()

# Email credentials
sender_email = "TaskManagerApp2025@gmail.com"
receiver_email = "buithaian321@gmail.com"  # for example
subject = "Important email from TaskMaster app"
body = "Just testing:)))"

send_email(sender_email, receiver_email, subject, body, app_password)


conn.commit()
cur.close()
