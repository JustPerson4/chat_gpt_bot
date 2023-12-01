import sqlite3
from datetime import datetime

connection = sqlite3.connect('users.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users(id PRIMARIY KEY AUTOINCERMENT INTEGER,tg_id INTEGER,phone_number TEXT,first_name TEXT,reg_data DATETIME);')

sql.execute('CREATE TABLE IF NOT EXISTS user_data(id PRIMARIY KEY AUTOINCERMENT INTEGER,telegram_id INTEGER,user_question TEXT,date DATETIME);')

def register_user(first_name,tg_id,phone_number):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    
    sql.execute('INSERT INTO users(first_name,tg_id,phone_number,reg_data) VALUES(?,?,?,?)',(first_name,tg_id,phone_number,datetime.now()))
    
    connection.commit()
    connection.close()
    
def check_user(tg_id):


    connection = sqlite3.connect("users.db")
    sql = connection.cursor()

    user = sql.execute("SELECT tg_id FROM users WHERE tg_id = ?",(tg_id,)).fetchone()




    if user:
        return True
    else:
        return False



def add_user_data(telegram_id,user_question):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    
    sql.execute('INSERT INTO user_data(telegram_id,user_question,date) VALUES(?,?,?)',(telegram_id,user_question,datetime.now()))
    connection.commit()
    connection.close()
    
def delete_user_data(telegram_id):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    
    sql.execute('DELETE FROM user_data WHERE telegram_id=?',(telegram_id,))
    
    connection.commit()
    connection.close