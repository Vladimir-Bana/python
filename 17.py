                #№1
# spisok=[1,2,3,4,5,6,7,8,9,10]
# spisok_1=[a for a in spisok]
# for i in spisok:
#     spisok_1.append(i)
# print(spisok_1)
                #№2
# spisok=[1,2,3,4,5,6,7,8,9,10]
# spisok_1=[a**2 for a in spisok]
# for i in spisok:
#     spisok_1.append(i)
# print(spisok_1)
                #№3
# spisok=[1,2,3,4,5,6,7,8,9,10]
# spisok_1=[]
# for i in spisok:
#     if i > 5:
#         spisok_1.append(i)
# print(spisok_1)
                #№4
# spisok=[1,2,3,4,5,6,7,8,9,10]
# spisok_1=[a for a in spisok if a>5]
#     for i in spisok:
#     if i > 5:
#     spisok_1.append(i)
# print(spisok_1)
                #№5
# spisok=[1,2,3,4,5,6,7,8,9,10]
# spisok_1=[i for i in spisok if i > 5 and i%2==0]
# for i in spisok:
#     if i > 5 and i%2==0:
#     spisok_1.append(i)
# print(spisok_1)
                #№6
# spisok=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# spisok_1=[i if i>5 else "Error" for i in spisok]
# for i in spisok:
#     if i>5:
#     spisok_1.append(i)
#     else:
#     spisok_1.append("Error")
# print(spisok_1)
                #№7
# spisok=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# spisok_1=["true_2" if i%2==0 else "true_3" if i%3==0 else "folse" for i in spisok]
# for i in spisok:
#     if i%2==0:
#     spisok_1.append("true_2")
#     elif i%3==0:
#     spisok_1.append("true_3")
#     else:
#     spisok_1.append("folse")
# print(spisok_1)
                #№8
# spisok=[1,2,3]
# spisok_1=[4,5,6]
# spisok_global=[(i,x) for i in spisok for x in spisok_1]
# for i in spisok:
#     for x in spisok_1:
#     spisok_global.append((i,x))
# print(spisok_global)
                #№9
# spisok=[1,2,3]
# spisok_1=[4,5,6]
# spisok_global=[(i,x) for i in spisok for x in spisok_1]
# for i in spisok:
#     for x in spisok_1:
#         spisok_global.append((i,x))
#         print(spisok_global)
#         for a in spisok_global:
#             print(a)
                #№10
# spisok=[5 for i in range(10)]
# print(spisok)
                #№11
# a="Рефреджиратор"
# spisok=[i*5 for i in a]
# print(spisok)
                #№12
# import random
# spisok=[random.randint(5,10) for i in range(10)]
# print(spisok)