#class Human:
#    pass
#p1=Human()
#p1.name="Vova"
#p1.surname="Nedbaevsikie"
#p1.place_of_birth="UA"
#p1.year_of_birth=2006
#p1.age=15
#print(p1.name)
#print(f"Name: {p1.name},Surname: {p1.surname},place_of_birth: {p1.place_of_birth},year_of_birth: {p1.year_of_birth},age: {p1.age}")


#class Human:
#    def __init__(self,name,surname,place_of_birth,year_of_birth,age):
#        self.name=name
#        self.surname=surname
#        self.place_of_birth=place_of_birth
#        self.year_of_birth=year_of_birth
#        self.age=age
#        print("Человек создан")
#    def hello(self):
#        print(f"Name: {p1.name},Surname: {p1.surname},place_of_birth: {p1.place_of_birth},year_of_birth: {p1.year_of_birth},age: {p1.age}")
#    def ages(self, n):
#        a=int(input())
#        return a-self.year_of_birth
#n=int(input())
#p1=Human("Den","Dmitriev","UA",1997,24)
#p1.hello()
#p2=Human("Vova","Nedb","UA",2006,15)
#p2.hello()
#print(p1.ages(n))

import math
class circle:
    pi=3.14
    c=0
    def __init__(self , rad):
        self.rad = rad
        circle.c+=1
    def len_c(self):
        return self.pi*self.rad**2
    def s(self):
        return 2*self.pi*self.rad
rad = int(input("="))
kolo1=circle(rad)
t = kolo1.len_c()
y = kolo1.s()
print(t)
print(y)
kolo2=circle(9)
i= kolo2.len_c()
u=kolo2.s()
print(i)
print(u)
print(circle.c)
