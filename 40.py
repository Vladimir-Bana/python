import sqlite3
from random import  randint

bd=sqlite3.connect("user.bd")
sql=bd.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    name TEXT,
    surname TEXT,
    login TEXT,
    password TEXT
)""")
bd.commit()
def reg():
    user_name = input("Введите ваше имя:")
    user_surname = input("Введите вашу фамилию:")
    user_login = input("Придумайте логин:")
    user_password = input("Придумайте пароль:")
    sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES (?,?,?,?)", (user_name,user_surname,user_login, user_password))
        bd.commit()
        print("Зарегистрировано!")
    else:
        print("Такая запись уже имеется")

    for i in sql.execute("SELECT * FROM user"):
        print(i)

def login():
    user_login=input("Введите логин: ")
    sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        print("Пройдите регестрацию!")
        reg()
    else:
        for i in sql.execute("SELECT login FROM user"):
            print(f"Добро пожаловать! {i}")
def start():
    login()

start()