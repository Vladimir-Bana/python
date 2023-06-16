    #1
# def name(a):
#     print(f"Привет{a}")
# a=input("=")
# name(a)
    #2
# def chisla(n):
#     print(n)
# n=int(input("="))
# chisla(n)
    #3
# def maxim(a,b):
#     if a>b:
#         print(f" bolshe {a}")
#     elif a<b:
#         print(f" bolshe {b}")
#     else:
#         print("equal")
# a=int(input("="))
# b=int(input("="))
# maxim(a,b)
    #4
# def m(a,b,c):
#     d=max(a,b,c)
#     print(d)
# a=int(input("="))
# b=int(input("="))
# c=int(input("="))
# m(a,b,c)
    #5
# def trik(a,b,c):
#     if a+b<=c and a+c<=b and b+c<=a:
#         print("Треугольника не существует")
#     else:
#         print("Треугольник существует")
# a=int(input("="))
# b=int(input("="))
# c=int(input("="))
# trik(a,b,c)
    #6
# def slova(a,b):
#     print(f"слова соеденены: {a}{b}")
# a=input("=")
# b=input("=")
# slova(a,b)
    #7
# def mat(a,b,c):
#     if c=="+":
#         print(a+b)
#     elif c=="-":
#         print(a-b)
#     elif c=="*":
#         print(a*b)
#     elif c=="/":
#         print(a/b)
#     else:
#         print("Unknown operation")
# a=int(input("="))
# b=int(input("="))
# c=input("=")
# mat(a,b,c)
    #8
# def html(a,b):
#     print(f"<{a}>{b}</{a}>")
# a=input("Введите тег=")
# b=input("Введите рядок=")
# html(a,b)
    #9
# def pori_roky(a):
#     if a=12 or a=1 or a=2:
#         print("Winter")
#     elif a=3 or a=4 or a=5:
#         print("Spring")
#     elif a=6 or a=7 or a=8:
#         print("Summer")
#     elif a=9 or a=10 or a=11:
#         print("Autumn")
#     else:
#         print("Нету такого месяца")
# a=int(input("месяц"))
# pori_roky(a)
    #10
# def math(a):
#     for i in a:
#         print("*"*i)
# math([2,7,1,4,2,3,9,3])
    #11
# def par(a):
#     if a%2==0:
#         print("число парное")
#     else:
#         print("Не парное")
# a=int(input("chislo="))
# par(a)
    #12
# import random
# def posled():
#     arr = [random.randint(1,100) for i in range(7)]
#     print(arr)
#     print(arr[0], arr[-1])
# posled()
    #13
# def fact(a):
#     f=1
#     for i in range(2, a+1):
#         f *= i
#     print(f)
# a = int(input())
# fact(a)