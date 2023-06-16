                #№1
# def greet_user():
#     print("Hello!")
# greet_user()
                #№2
# def summa(a1, b1):
#     global c
#     c = a1+b1
# a = int(input("Введите первое число ---> "))
# b = int(input("Введите второе число ---> "))
# summa(a, b)
# print(c)
                #№3
# def digit(p):
#     print ("1"*p)
# n = int(input("введите число сколько вы хотите получить символов --> "))
# x = int(input("введите число сколько вы хотите получить символов --> "))
# digit(n)
# digit(x)
                #№4
# def digit(a, b):
#     c = a*b
#     print(c)
# z = int(input("введите число сколько вы хотите получить символов --> "))
# d = str(input("введите символ 1--> "))
# v = int(input("введите число сколько вы хотите получить символов --> "))
# u = str(input("введите символ 2--> "))
# digit(d, z)
# digit(u, v)               
                #№5
# def greet_user(username, userlast):
#     print(f"Hello, {username.title()} {userlast.title()}!")
# name = input("Name --> ")
# name_1 = input("Last name --> ")
# greet_user(name, name_1)                
                #№6
# def max2(a, b):
#     if a > b : m = a
#     else: m = b
#     return m
# q = max2(5, 2)
# print("max =", q)
                #№7
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':break
#     l_name = input("Last name: ")
#     if l_name == 'q':break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")