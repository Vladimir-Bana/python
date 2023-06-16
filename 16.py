                #№1
# def month_to_season(nomer_mesaca):
#     if nomer_mesaca==12 or 1<=nomer_mesaca <=2:
#              print("Зима")
#     elif 3<=nomer_mesaca <=5:
#              print("Весна")
#     elif 6<=nomer_mesaca <=8:
#              print("Лето")
#     elif 9<=nomer_mesaca <=11:
#              print("Осень")
#     else:
#         print("error")
# nomer=int(input("Ведите номер месяца -->"))
# month_to_season(nomer)
                    #№2
# user_1={"color":"red","speed":"slow","coins":5}
# user_2={"color":"red","speed":"slow","coins":5}
# user_3={"color":"red","speed":"slow","coins":5}
# global_user=[user_1,user_2,user_3]
# print(global_user)
# for i in global_user:
#     print(i)
                    #№3
# users=[]
# for i in range(59):
#     new_user={"color":"red","speed":"slow","coins":5}
#     users.append(new_user)
# print(users)
# for z in users:
#     print(z)
# print("-"*60)
# print(f"В игре {len(users)}игроков")
                    #№4
# users=[]
# for i in range(59):
#     new_user={"color":"red" , "speed":"slow" , "coins":5}
#     users.append(new_user)
# print(users)
# for x in users[8:16]:
#     if x["color"]=="red":
#         x["color"]="green"
#         x["speed"]="meedl"
#         x["coins"]=15
# for z in users:
#     print(z)
# print("-"*60)
# print(f"В игре {len(users)} игроков")
                    #№5
# users={
#     "Zhenya":["task1","task2","task3","task4"],
#     "Sasha":["task1","task2"],
#     "Den":["task1"],
#     "Vova":["task1","task2","task3","task4","task5","task6"],
#     "Vlad":["task1","task2","task3","task4","task5","task6","task7","task8","task9","task10"]
#     }
# for z,x in users.items():
#     print("-"*40)
#     print(f"Его зовут {z} , он решил такие задачи : ")
#     for task in x:
#         print(f"\t\/{task}")
#     print("-"*40)                    
                    #№6
# def month_seasons(n,value):
#     for z,x in month.items():
#         if n in z:
#             value=x
#             break
#         elif n>12 and n<1:
#             print(none)
#             break
#     return value
# month={
#     (12,1,2):"winter",
#     (3,4,5):"spring",
#     (6,7,8):"summer",
#     (9,10,11):"autumn"
#     }
# none=f"error"
# About=int(input("ведите номер месяца : "))
# print(month_seasons(About,none))