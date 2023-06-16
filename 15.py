                #№1
# korteg=("Zheka","Vova","Python",132,222)
# print(korteg)
# print(korteg[1])
# print(korteg[2])
# print(korteg[-1])
# print(korteg[-2])
# for i in korteg:
#     print(i)                
                #№2
# korteg=("Zheka","Vova","Python",132,222)
# a = korteg.index("Python")
# print(a)
# last = korteg.index(222)
# print(last)
                #№3
# kor_int=(10,15,10,10,777,375,15)
# a = kor_int.count(10)
# print(a)
# b = kor_int.count(15)
# print(b)
# summ=0
# for i in kor_int:
#     summ+=i
# print(summ)
# v = sum(kor_int)
# print(v)
# x = min(kor_int)
# print(x)
# c = max(kor_int)
# print(c)                
                #№4
# kort=("Python","Java","JavaScript","Html")
# print(kort)
# kort=(1,2)
# print(kort)                
                #№5
# name={"Denis":24,"Zheka":17,"Vova":15,"Bogdan":17,"Misha":2}
# print(name)
# p = name["Denis"]
# print(p)
# a = name["Zheka"]
# print(a)                
                #№6
# name_1={"Deniasdsds":24,"Zheasdka":17,"Vovasda":15,"Boasdasdgdan":17,"Mishasddsada":2}
# name={"Denis":24,"Zheka":17,"Vova":15,"Bogdan":17,"Misha":2}
# our_cars={"Tiger Porshe":1943,"Camaro":1984,"Ferrari":103,"Lada":2004,"Bugati":2000}
## metod 1
# python = name.copy()
# python.update(our_cars)
# print(python)
## metod2
# olds=name | our_cars | name_1
# print(olds)                
                #№7
# name_1={"Deniasdsds":24,"Zheasdka":17,"Vovasda":15,"Boasdasdgdan":17,"Mishasddsada":2}
# print(name_1.keys())
# for i in name_1.keys():
#     print(i)
# print(name_1.values())
# for b in name_1.values():
#     print(b)
# for c,f in name_1.items():
#     print(f"Меня зовут {c} и мне {f} лет ")                
                #№8
# name_1={"Deniasdsds":24,"Zheasdka":17,"Vovasda":15,"Boasdasdgdan":17,"Mishasddsada":2}
# print(name_1.clear())
# print(name_1)  
                #№9
# name_1={"Denis":24,"Zheka":17,"Vova":15,"Bodan":17,"Misha":2}
# a = name_1.get("Ilya","User not defaund")
# print(a)
# name_1={"Denis":24,"Zheka":17,"Vova":15,"Bodan":17,"Misha":2}
# a = name_1.get("Vova","User not defaund")
# print(a)                