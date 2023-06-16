import sqlite3
from random import randint


bd=sqlite3.connect("user.bd")
sql=bd.cursor() # создает, изменяет, удаляет

sql.execute("""CREATE TABLE IF NOT EXISTS user(
  login TEXT,
  password TEXT,
  cash INT
)""")

bd.commit() # подтверждение действий

def reg():
  user_login=input("login:")
  user_password=input("password:")
  sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")

  if sql.fetchone() is None: #проверка первого элемента
    sql.execute(f"INSERT INTO user VALUES (?,?,?)", (user_login,user_password,0))
    bd.commit()
    print("Зарегистрировано!")
  else:
    print("Такая запись уже имеется")

  for i in sql.execute("SELECT * FROM user"): # выбрать все значения с юзера
    print(i)

def casino():
  user_login=input("login:")
  number = randint(0, 1)

  # for i in sql.execute(f"SELECT cash FROM user WHERE login='{user_login}'"):
  #   result=i[0] # если б не было кв. скобок, то выводилось бы 0,
  sql.execute(f"SELECT cash FROM user WHERE login='{user_login}'")
  result=sql.fetchone()[0]

  sql.execute(f"SELECT login FROM user WHERE login='{user_login}'")
  if sql.fetchone() is None:
    print("Такого пользователя нету")
    reg()
  else:
    if number == 1:
      sql.execute(f"UPDATE user SET cash={1000+result} WHERE login='{user_login}'")
      bd.commit()
      print("Вы выиграли!")
    else:
      print("Вы проиграли")

def write():
  for i in sql.execute("SELECT login, cash FROM user"): # выбрать все значения с юзера
    print(i)

def start():
  casino()
  write()

start()