                #№1
# klient=["Сайт1","Сайт2","Сайт3","Сайт4"]
# mykompany=[]
# while klient:
#     c1=klient.pop(0)
#     print(f"Сайт {c1} в разработке")
#     mykompany.append(c1)
# for el in mykompany:
#     print(f"{el} готов")
# print(mykompany)
                #№2
# #подпрограммы
# def site():
#     while mass1:
#         c1=mass1.pop(0)
#         print(f"Сайт {c1} в разработке")
#         mass2.append(c1)
# def complete():
#     for el in mass2:
#         print(f"{el} готов")
# #основной код
# mass1=["Сайт1","Сайт2","Сайт3","Сайт4"]
# mass2=[]
# site()
# complete()
                #№3
# def menu(sizes,*Bogdan):
#     print(f"Вы выбрали такие пиццы, c размером {sizes}:")
#     for i in Bogdan:
#         print(f"-{i}")
# size=input("Введите размер пиццы")
# menu(size,"Четыре мяса")
# menu(size,"Гаваи","Четыре сыра","Вова")