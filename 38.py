import sqlite3
from random import  randint

bd=sqlite3.connect("user.bd")
sql=bd.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)""")
bd.commit()
def reg():
    user_login = input("login:")
    user_password = input("password:")
    user_cash = 0
    sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES (?,?,?)", (user_login, user_password, user_cash))
        bd.commit()
        print("Зарегистрировано!")
    else:
        print("Такая запись уже имеется")

    for i in sql.execute("SELECT * FROM user"):
        print(i)

def casino():
    user_login=input("Введите логин: ")
    for i in sql.execute(f"SELECT cash FROM user WHERE login='{user_login}'"):
        result=i[0]
    number=randint(0,1)
    sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        print("Пройдите регестрацию!")
        reg()
    else:
        if number==1:
            sql.execute(f"UPDATE user SET cash={1000+result} WHERE login='{user_login}'")
            print("ВЫ ВЫГРАЛИ 1000 очков!")
            bd.commit()
        else:
            sql.execute(f"UPDATE user SET cash={result-500} WHERE login='{user_login}'")
            print("НЕУДАЧА(")
            bd.commit()
def all_data():
    for i in sql.execute("SELECT login,cash FROM user"):
        print(i)
def start():
    casino()
    all_data()

start()