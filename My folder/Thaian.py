# ===============IMPORTANT THINGS AREA===============:

# ! important variables!!!:
app_password: str = "fimhhmpykyoyaxuc"  # ! do not touch on this varible
# ! important variables!!!

# ====================IMPORTING AREA====================:

from PyQt6.QtWidgets import QMainWindow,QApplication,QLineEdit,QMessageBox, QPushButton
from PyQt6 import uic
import sys
import database
import sqlite3
import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# ==============CLASS EXCEPTIONS AREA==============:


class InvaildEmail(Exception):
    """a custom exception name InvaildEmail

    Args:
        Exception (type): the Exception class
    """

    def __init__(self, email: str, message="Invaild email"):
        self.mesage = message
        self.email = email
        super().__init__(f"{message}: {email}")


class InvaildPassword(Exception):
    """a custom exception name InvaildPassword

    Args:
        Exception (type): the Exception class
    """

    def __init__(self, password: str, message="Invaild password"):
        self.mesage = message
        self.email = password
        super().__init__(f"{message}: {password}")


# ====================NORMAL CLASSES AREA====================:


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
        """This method is for __init__ method for checking if this email is valid or not

        Returns:
            bool: return True if this email is valid and not if this email isn't valid
        """
        return re.match(self.EMAIL_REGEX, self.address) is not None

    def returns_email(self) -> str:
        return self.address

    def taskmanagerapp2025_send_email(
        self, subject: str, body: str, app_password: str = app_password
    ):
        """This method send an email

        Args:
            reciver_email (str): the reciver of the email
            subject (str): the subject of the email
            body (str): the body of the email
            app_password (str): # !THIS EMAIL CAN BE SEND OR CAN'T BE SEND DEPENDS ON THIS app_password VARIABLE
        """
        # Set up the MIME messagexc
        msg = MIMEMultipart()
        msg["From"] = "taskmanagerapp2025@gmail.com"
        msg["To"] = self.address
        msg["Subject"] = subject

        # Add the body of the email
        msg.attach(MIMEText(body, "plain"))

        # Set up the SMTP server
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Secure the connection
            server.login(
                "taskmanagerapp2025@gmail.com", app_password
            )  # Login using App Password
            server.sendmail(
                "taskmanagerapp2025@gmail.com", self.address, msg.as_string()
            )
            server.quit()

            print("Email sent successfully!")

        except Exception as e:
            print(f"Failed to send email: {repr(e)}")


class Password:
    """a password type

    Raises:
        InvaildPassword: raise this if the password is invaild

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
        have_alpha = False
        have_alpha_upper = False
        have_symbol = False
        for i in self.__alphabet:
            if i in self.password:
                have_alpha = True

        for i in self.__upper_alphabet:
            if i in self.password:
                have_alpha_upper = True

        for i in self.__alphabet:
            if i in self.password:
                have_symbol = True
        return have_alpha and have_alpha_upper and have_symbol is not None

    def return_password(self) -> str:
        return self.password
#==========================QT CLASSES AREA==========================

class Alert(QMessageBox):
    def error_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()
        
    def success_message(self, message):
        self.setIcon(QMessageBox.Icon.Information)
        self.setText(message)
        self.setWindowTitle('Success')
        self.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Qt/ui/login.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email == '':
            msg = Alert()
            self.email_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            self.password_input.setFocus()
            return
        
        user = database.find_user_by_email_and_password(email,password)
        if user:
            msg = Alert()
            msg.success_message('Login succesful')
            
        else:
            msg = Alert()
            msg.error_message('invalid email or password')
            
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()
        
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui('Qt/ui/register.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.name_input = self.findChild(QLineEdit, 'name_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.confirm_password_input = self.findChild(QLineEdit, 'confirm_password_input')
        
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        
    def register(self):
        email = self.email_input.text()
        name = self.name_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        if email == '':
            msg = Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        if name == '':
            msg = Alert()
            msg.error_message('Please enter name')
            self.name_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
        
        if password != confirm_password:
            msg = Alert()
            msg.error_message('Password and confirm passord does not match')
            self.confirm_password_input.setFocus()
            return
        
        user = database.find_user_by_email(email)
        if user:
            msg = Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email, email, password)
            msg = Alert()
            msg.success_message('Registration successful')
            self.close()
            

# ====================FUNCTION AREA====================:



# ====================CODE TEST AREA====================:

def main():
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()

    username: str = input("Enter your username: ")
    while True:
        email:str = input("Enter your email: ")
        try:
            user_email:type = Email(email)
        except InvaildEmail as e:
            print(f"Error: {repr(e)}")
        else:
            break

    while True:
        password:str = input(
            "Enter your password (include lower and uppercase letters, symbols): "
        )
        try:
            user_password:type = Password(password)
        except InvaildPassword as e:
            print(f"Error: {repr(e)}")
        else:
            break

    cur.execute(
        """INSERT INTO users (username,email,password) VALUES (?,?,?)""",
        (username, user_email.returns_email(), user_password.return_password()),
    )

    user_email.taskmanagerapp2025_send_email(
        user_email, "test", "hello there!, this is a test email from taskmanagerapp2025"
    )

    conn.commit()
    cur.close()

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())
