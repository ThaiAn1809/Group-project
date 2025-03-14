import sqlite3

def create_user(email, name, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user(email, name, password) VALUES (?, ?, ?)', (email, name, password))
    conn.commit()
    conn.close()
    
def find_user_by_email(email):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email, name, password FROM user WHERE email = ?', (email, ))
    user = cursor.fetchone()
    conn.close()
    return user

def find_user_by_email_and_password(email, password):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email, name, password FROM user WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

